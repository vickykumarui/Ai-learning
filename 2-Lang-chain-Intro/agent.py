

import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
     api_key = os.getenv('GROQ_API_KEY'),
     base_url="https://api.groq.com/openai/v1",
)

PRICES = {"shoes": 799, "hat": 399, "bag": 1420, "shorts": 1299, "pants": 1699}

def get_price(item):
    print(f"🔧 tool called: get_price({item})")     # so you SEE it happen
    return f"₹{PRICES.get(item.lower(), 'unknown')}"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_price",
            "description": "Get the price of shop item user asked for",
            "parameters": {
                "type": "object",
                "properties":{
                    "item": {
                        "type": "string",
                        "description": "the item name",
                        "required": ["item"],
                    }
                }
            }
        }
    }
]

def agent(user_message):
    messages = [{
        "role": "user",
        "content": user_message,
    }]

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools
    )

    msg = response.choices[0].message
    # print("msg", msg)
    if msg.tool_calls:
        messages.append(msg)
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments)
            name = call.function.name
            result = get_price(args["item"])
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

        response =client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
        )
        msg = response.choices[0].message
    return msg

print("How much are the shoes", agent("How much are the shoes"))
print("How are you", agent("How are you"))