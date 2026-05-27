from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Weather Server")


@mcp.tool()
def get_weather(latitude: float, longitude: float) -> str:
    """Get current weather for a location."""

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current_weather=true"
    )

    response = requests.get(url)
    data = response.json()

    weather = data["current_weather"]

    return (
        f"Temperature: {weather['temperature']}°C, "
        f"Wind speed: {weather['windspeed']} km/h"
    )


if __name__ == "__main__":
    print("RUN")
    mcp.run()