import os
from openai import OpenAI
from dotenv import load_dotenv
from scrapper import fetch_website_contents

load_dotenv()

client = OpenAI(
    api_key = os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1",
)

system_prompt = """You are website summarizer 
Give a short summary. Ignore navigation menus
Respond in markddown format
"""

def summarize(url):
    website_contents = fetch_website_contents(url)
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages= [
            {"role": 'system', "content": system_prompt},
            {"role": 'user', "content": website_contents}

        ]
    )

    return response.choices[0].message.content
