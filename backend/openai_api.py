import os
import openai
from config import (
    OPENAI_API_KEY,
)
from models import Chat

openai.api_key = OPENAI_API_KEY

import re
import openai

def generate_response(user_input, chat_id=None):
    chat = Chat.query.get(chat_id) if chat_id else None

    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    if chat:
        print(f"Chat history: {chat.chat_history}")
        for message in chat.chat_history:
            messages.append({"role": "user", "content": message.user_message})
            if message.bot_message: 
                messages.append({"role": "assistant", "content": message.bot_message})
    messages.append({"role": "user", "content": user_input})

    print(f"Messages: {messages}")

    completions = openai.ChatCompletion.create(
        model="gpt-4",
       ## model="gpt-3.5-turbo-16k",
        messages=messages,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.8,
    )

    print(f"Received message: {user_input}")
    print(f"Completions object: {completions}")

    response_text = completions.choices[0]['message'].get('content', '').strip()
    print(f"Generated response: {response_text}")
    return {"text": response_text}
