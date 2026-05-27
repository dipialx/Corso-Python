from redis_search import *
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

    context = redis_search(user_input)

    prompt = f"""
Use only the following context to answer the question.

Context:
{context}

Question:
{user_input}

"""
    print ("---prompt---", prompt)

    messages.append({
        "role": "user",
        "content": prompt
    })

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages,
        temperature=0
    )

    answer = response.choices[0].message.content

    print("Assistant:", answer)

    messages.append({
        "role": "assistant",
        "content": answer
    })


#test : Chi è dottor watson?
#test : Cos'è un pomodoro?
#test : In che modo Irene Adler riesce a battere Holmes?