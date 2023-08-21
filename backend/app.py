import os
from flask import (
    Flask,
    render_template,
    flash,
    session,
    abort,
    redirect,
    url_for,
    request,
    jsonify,
)
from config import (
    SECRET_KEY,
    GOOGLE_OAUTH_CLIENT_ID,
    GOOGLE_OAUTH_CLIENT_SECRET,
    OPENAI_API_KEY,
)
from sso import google_bp, refresh_google_token
from chat import process_message
from models import db, Chat, Message
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError, InvalidClientIdError


app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend/templates'),
            static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../frontend/static'))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)
with app.app_context():
    db.create_all()

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
app.config["SECRET_KEY"] = SECRET_KEY
app.config["GOOGLE_OAUTH_CLIENT_ID"] = GOOGLE_OAUTH_CLIENT_ID
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = GOOGLE_OAUTH_CLIENT_SECRET
app.config["OPENAI_API_KEY"] = OPENAI_API_KEY
app.secret_key = app.config['SECRET_KEY']
app.config["GOOGLE_OAUTH_CLIENT_ID"] = app.config['GOOGLE_OAUTH_CLIENT_ID']
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = app.config['GOOGLE_OAUTH_CLIENT_SECRET']
app.register_blueprint(google_bp, url_prefix="/login")

@app.route("/")
def index():
    theme_preference = 'theme-light'
    chat = Chat.query.filter_by(user_email=session.get("email")).first()

    if chat and chat.theme_preference:
        if chat.theme_preference == 'dark':
            theme_preference = 'theme-dark'
        elif chat.theme_preference == 'light':
            theme_preference = 'theme-light'
        elif chat.theme_preference == 'system':
            theme_preference = 'theme-system'

    if not google_bp.authorized:
        return render_template("login.html", theme_preference=theme_preference)

    try:
        refresh_google_token()
        resp = google_bp.session.get("/oauth2/v3/userinfo")
    except (TokenExpiredError, InvalidClientIdError):
        flash("Google Auth Expired - Re-Authenticate", category="error")
        return redirect(url_for("google.login", theme_preference=theme_preference))

    if resp.ok:
        user_info = resp.json()
        email = user_info["email"]
        domain = email.split("@")[-1]
       # if domain != "mydomain.com":
       #     flash("Access restricted to users with an mydomain.com email address.", category="error")
       #     return abort(403)

        session.update(
            {
                "name": user_info["name"],
                "given_name": user_info["given_name"],
                "family_name": user_info["family_name"],
                "picture": user_info["picture"],
                "email": email,
            }
        )
        return redirect(url_for("chat"))
    print("index()")
    return render_template("login.html", theme_preference=theme_preference)



@app.route("/chat")
def chat():
    if "email" not in session:
        return redirect(url_for("index"))

    chat = Chat.query.filter_by(user_email=session["email"]).first()
    theme_preference = 'theme-light'

    if chat and chat.theme_preference:
        if chat.theme_preference == 'dark':
            theme_preference = 'theme-dark'
        elif chat.theme_preference == 'light':
            theme_preference = 'theme-light'
        elif chat.theme_preference == 'system':
            theme_preference = 'theme-system'

    return render_template("chat.html", user_image_url=session["picture"], user_name=session["name"], theme_preference=theme_preference)


@app.route("/process_message", methods=["POST"])
def process_message_route():
    data = request.get_json()
    message = data["message"]
    new_chat = data.get("new_chat", False)
    response_type = data.get("response_type", "chat")
    chat_id = data.get("chat_id", None)

    if new_chat:
        chat = Chat(user_email=session["email"])
    elif chat_id is not None:
        chat = Chat.query.get(chat_id)
        if not chat:
            return jsonify({"error": "Chat not found"}), 404
    else:
        chat = Chat.query.filter_by(user_email=session["email"]).order_by(Chat.id.desc()).first()
        if not chat:
            chat = Chat(user_email=session["email"])

    db.session.add(chat)
    db.session.commit()

    response, error = process_message(message, response_type, chat.id)
    if error:
        return jsonify({"error": error})

    message = Message(chat_id=chat.id, user_message=message, bot_message=response)
    db.session.add(message)
    db.session.commit()

    return jsonify({"response": response, "chat_id": chat.id})


@app.route("/chat_history", methods=["GET"])
def chat_history():
    chats = Chat.query.filter_by(user_email=session["email"]).all()
    if not chats:
        return jsonify({"chats": []})

    chat_list = []
    for chat in chats:
        chat_list.append({
            "id": chat.id,
            "last_message": chat.chat_history[-1].user_message if chat.chat_history else ""
        })

    return jsonify({"chats": chat_list})


@app.route("/chat/<int:chat_id>", methods=["GET"])
def get_chat(chat_id):
    chat = Chat.query.get(chat_id)
    if not chat or chat.user_email != session["email"]:
        return jsonify({"error": "Chat not found"}), 404

    chat_history = []
    for message in chat.chat_history:
        chat_history.append({
            "user_message": message.user_message,
            "bot_message": message.bot_message
        })

    return jsonify({"chat_history": chat_history})


@app.route("/delete_chat/<int:chat_id>", methods=["DELETE"])
def delete_chat(chat_id):
    chat = Chat.query.get(chat_id)
    if not chat:
        return jsonify({"error": "Chat not found"}), 404

    Message.query.filter_by(chat_id=chat_id).delete()

    db.session.delete(chat)
    db.session.commit()

    return "", 204


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return "", 204


@app.route('/releases')
def releases():
    return render_template('releases.html')

@app.route('/terms-of-use')
def terms_of_use():
    return render_template("terms_of_use.html")

@app.route("/set_theme_preference", methods=["POST"])
def set_theme_preference():
    data = request.get_json()
    theme = data.get("theme")
    
    chat = Chat.query.filter_by(user_email=session["email"]).first()
    
    if chat:
        chat.theme_preference = theme
        db.session.commit()
        return jsonify({"message": "Theme preference updated"}), 200
    
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
   app.run(debug=False)
