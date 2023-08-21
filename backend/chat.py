from openai_api import generate_response
from banned_keywords import check_banned_keywords
from dalle_api import generate_image_response

def process_message(message, response_type, chat_id=None):
    banned_words, is_banned = check_banned_keywords(message)
    if is_banned:
        error = "Due to the data protection policies, your query cannot be sent or processed, due to the following banned words found in your query: " + ", ".join(banned_words)
        return None, error
    if response_type == "image":
        response = generate_image_response(message)
    else:
        response = generate_response(message, chat_id)

    return response['text'], None