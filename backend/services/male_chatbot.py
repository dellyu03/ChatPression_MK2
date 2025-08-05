from openai import OpenAI
from dotenv import load_dotenv
from pprint import pprint
import os


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client=OpenAI(api_key = openai_api_key)

model = "gpt-4o-mini-2024-07-18"

messages = [
    {"role": "system", "content" : "You are a helpful assistant"},
    {"role": "user", "content" :"who is the world champion in f1 2021"}
]

response = client.chat.completions.create(model=model, messages=messages).model_dump()
pprint(response)