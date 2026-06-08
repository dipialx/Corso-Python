from dotenv import load_dotenv
from openai import OpenAI
import os

# Carica il file .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite",
    temperature=0,
    max_tokens=1000,
    messages=[
        {"role": "system", "content": "Sei un insegnante di python"},
        {"role": "user", "content": "Spiegami pandas"}
    ]
)
print("ROLE", response.choices[0].message.role)
print("RISPOSTA", response.choices[0].message.content)