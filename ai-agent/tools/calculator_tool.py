from typing import Dict

def calculator(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Calculation error: {str(e)}"