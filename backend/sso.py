import os
from config import (
    GOOGLE_OAUTH_CLIENT_ID,
    GOOGLE_OAUTH_CLIENT_SECRET,
)
from flask import (
    Flask,
    flash,
    session,
)
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized
from time import time
from flask import redirect, url_for
from oauthlib.oauth2.rfc6749.errors import InvalidClientIdError

app = Flask(__name__)
app.config["GOOGLE_OAUTH_CLIENT_ID"] = GOOGLE_OAUTH_CLIENT_ID
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = GOOGLE_OAUTH_CLIENT_SECRET

app.secret_key = app.config['SECRET_KEY']
app.config["GOOGLE_OAUTH_CLIENT_ID"] = app.config['GOOGLE_OAUTH_CLIENT_ID']
app.config["GOOGLE_OAUTH_CLIENT_SECRET"] = app.config['GOOGLE_OAUTH_CLIENT_SECRET']

google_bp = make_google_blueprint(
    client_id=app.config["GOOGLE_OAUTH_CLIENT_ID"],
    client_secret=app.config["GOOGLE_OAUTH_CLIENT_SECRET"],
    scope=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid",
    ],
    offline=True,
    reprompt_consent=False,
)

app.register_blueprint(google_bp, url_prefix="/login")

@oauth_authorized.connect_via(google_bp)
def google_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with Google.", category="error")
        return False

    resp = blueprint.session.get("/oauth2/v3/userinfo")
    if not resp.ok:
        flash("Failed to fetch user information.", category="error")
        return False

    user_info = resp.json()
    email = user_info["email"]

    session["token"] = token
    session["token_expires_at"] = time() + token["expires_in"]
    session["refresh_token"] = token.get("refresh_token")

    flash(f"Successfully logged in with Google as {email}.", category="success")
    return True


def refresh_google_token():
    if (
        "token" not in session
        or "token_expires_at" not in session
        or "refresh_token" not in session
    ):
        return

    if time() > session["token_expires_at"] - 60:
        blueprint = google_bp

        try:
            response = blueprint.session.post(
                "https://www.googleapis.com/oauth2/v4/token",
                data={
                    "grant_type": "refresh_token",
                    "client_id": blueprint.client_id,
                    "client_secret": blueprint.client_secret,
                    "refresh_token": session["refresh_token"],
                },
            )
        except InvalidClientIdError:
            flash("Google Auth Expired - Re-Authenticate", category="error")
            return redirect(url_for("google.login"))


        if response.ok:
            token = response.json()
            session["token"] = token
            session["token_expires_at"] = time() + token["expires_in"]
            print("Access token refreshed successfully") 
        else:
            flash("Failed to refresh the access token.", category="error")
            print("Failed to refresh the access token")  
            print(response.text)