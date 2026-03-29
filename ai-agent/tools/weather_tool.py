
import requests

import requests

def weather(city: str) -> str:
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return "Weather unavailable"
        return response.text
    except Exception as e:
        return f"Weather error: {str(e)}"