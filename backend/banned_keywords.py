BANNED_KEYWORDS = [
    "keyword1",
    "keyword2",
    "keyword3",
]

def check_banned_keywords(message):
    banned_words = [word for word in BANNED_KEYWORDS if word.lower() in message.lower()]
    is_banned = bool(banned_words)
    print("check_banned_keywords()")
    return banned_words, is_banned