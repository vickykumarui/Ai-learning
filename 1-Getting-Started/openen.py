import os
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI(

)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b", # to run this we need openai api key that's why we are using groq apikey which is free
     messages=[
            {"role": 'system', "content": "You are travel agent"},
            {"role": 'user', "content": "Suggest one good thing about bangalore"}
        ]
)
