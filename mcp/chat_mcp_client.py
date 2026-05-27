import asyncio
import json
import os
from pathlib import Path
from contextlib import AsyncExitStack
from dotenv import load_dotenv
from openai import OpenAI

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

BASE_DIR = Path(__file__).parent

llm = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools = [
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


async def open_mcp_session(stack, filename):
    server_params = StdioServerParameters(
        command="python",
        args=[str(BASE_DIR / filename)]
    )

    read, write = await stack.enter_async_context(
        stdio_client(server_params)
    )

    session = await stack.enter_async_context(
        ClientSession(read, write)
    )

    await session.initialize()

    return session


async def main():
    async with AsyncExitStack() as stack:

        geocoding_session = await open_mcp_session(
            stack,
            "geocoding_server.py"
        )

        weather_session = await open_mcp_session(
            stack,
            "weather_server.py"
        )

        tool_sessions = {
            "geocode": geocoding_session,
            "get_weather": weather_session
        }

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

            while True:
                response = llm.chat.completions.create(
                    model="gemini-2.5-flash",  #gemini-2.0-flash-lite
                    messages=messages,
                    temperature=0,
                    tools=tools
                )

                message = response.choices[0].message

                if not message.tool_calls:
                    answer = message.content
                    print("Assistant:", answer)

                    messages.append({
                        "role": "assistant",
                        "content": answer
                    })

                    break

                messages.append(message)

                for tool_call in message.tool_calls:
                    tool_name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)

                    print("\nCalling MCP tool:", tool_name)
                    print("Arguments:", args)

                    session = tool_sessions[tool_name]

                    tool_result = await session.call_tool(
                        tool_name,
                        arguments=args
                    )

                    result_text = tool_result.content[0].text

                    print("Tool result:", result_text)

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result_text
                    })


if __name__ == "__main__":
    asyncio.run(main())