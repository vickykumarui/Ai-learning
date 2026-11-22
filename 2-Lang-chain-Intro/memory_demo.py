import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-120b",
    api_key = os.getenv('GROQ_API_KEY'),
    base_url="https://api.groq.com/openai/v1",
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are friendly tutor"),
    MessagesPlaceholder("history"),
    ("human","{question}")
])

chain = prompt | model

history = [HumanMessage('My name is vicky'), AIMessage('Hi Vicky')]

print(chain.invoke({"history": history, "question": "What is my name" }).content)