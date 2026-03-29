
from google import genai
from config import GEMINI_API_KEY, MODEL_NAME
from memory import MemoryManager

from tools.calculator_tool import calculator
from tools.time_tool import get_time
from tools.weather_tool import weather
from tools.translator_tool import translate
from tools.file_reader_tool import read_file

class Agent:
    def __init__(self, memory: MemoryManager):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.memory = memory

    def run(self, user_input: str):
        self.memory.add("user", user_input)

        try:
            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=self.memory.get(),
                config={
                    "tools": [calculator, get_time, weather, translate, read_file]
                },
            )

            text = response.candidates[0].content.text
            self.memory.add("model", text)
            return text
        except Exception as e:
            return f"Agent error: {str(e)}"