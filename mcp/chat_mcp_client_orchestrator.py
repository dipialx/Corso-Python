import asyncio
import json
import os
from contextlib import AsyncExitStack
from dotenv import load_dotenv
from openai import OpenAI

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools=tools = [
    {
        "type": "function",
        "function": {
            "name": "geocode",
            "description": "Get latitude and longitude for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather from latitude and longitude",
            "parameters": {
                "type": "object",
                "properties": {
                    "latitude": {"type": "number"},
                    "longitude": {"type": "number"}
                },
                "required": ["latitude", "longitude"]
            }
        }
    }
]

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["weather_server.py"]
    )

    async with AsyncExitStack() as stack:
        read, write = await stack.enter_async_context(stdio_client(server_params))

        session = await stack.enter_async_context(
            ClientSession(read, write)
        )

        await session.initialize()

        print("=== MCP Weather Chat ===")
        print("Type 'exit' to quit\n")

        messages = [
            {
                "role": "system",
                "content": """
        You are a weather assistant.

        When the user asks for weather in a city:
        1. First call geocode to get latitude and longitude.
        2. Then call get_weather with those coordinates.
        3. Answer the user using the weather result.
        """
            }
        ]
        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                break

            messages.append({
                "role": "user",
                "content": user_input
            })

            response = llm.chat.completions.create(
                model="gemini-2.5-flash",  #gemini-2.0-flash-lite
                messages=messages,
                temperature=0,
                tools=tools
            )

            message = response.choices[0].message

            if message.tool_calls:
                tool_call = message.tool_calls[0]

                args = json.loads(tool_call.function.arguments)

                print("\nCalling MCP tool:", tool_call.function.name)
                print("Arguments:", args)

                tool_result = await session.call_tool(
                    tool_call.function.name,
                    arguments=args
                )

                result_text = tool_result.content[0].text

                messages.append(message)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result_text
                })

                final_response = llm.chat.completions.create(
                    model="gemini-2.5-flash",  #gemini-2.0-flash-lite
                    messages=messages,
                    temperature=0
                )

                answer = final_response.choices[0].message.content

            else:
                answer = message.content

            print("Assistant:", answer)

            messages.append({
                "role": "assistant",
                "content": answer
            })


if __name__ == "__main__":
    asyncio.run(main())