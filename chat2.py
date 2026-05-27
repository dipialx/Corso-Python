from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


messages = []

while True:
    user_input = input("You: ")

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages
    )

    answer = response.choices[0].message.content

    print("Assistant:", answer)

    messages.append({
        "role": "assistant",
        "content": answer
    })