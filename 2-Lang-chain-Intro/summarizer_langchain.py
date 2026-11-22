import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from scrapper import fetch_website_contents

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Give short friendly summary of this website:\n\n{website}"
)

model = ChatOpenAI(
    model="openai/gpt-oss-120b",
    api_key = os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1",
) 

parser = StrOutputParser()

chain = prompt | model | parser


def summarizer(url):
    return chain.invoke(fetch_website_contents(url))

print(summarizer("https://www.wikipedia.org/"))

