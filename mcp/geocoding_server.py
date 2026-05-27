from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Geocoding Server")


@mcp.tool()
def geocode(city: str) -> dict:
    """
    Get latitude and longitude for a city.
    """

    url = (
        "https://nominatim.openstreetmap.org/search"
        f"?q={city}"
        "&format=json"
        "&limit=1"
    )

    headers = {
        "User-Agent": "mcp-demo"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    if not data:
        return {
            "error": "City not found"
        }

    return {
        "latitude": float(data[0]["lat"]),
        "longitude": float(data[0]["lon"])
    }


if __name__ == "__main__":
    mcp.run()