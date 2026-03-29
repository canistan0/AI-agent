import os

def read_file(path: str) -> str:
    if not os.path.exists(path):
        return "File does not exist"
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return f"File read error: {str(e)}"