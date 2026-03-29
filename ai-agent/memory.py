
class MemoryManager:
    def __init__(self):
        self.history = []

    def add(self, role: str, content: str):
        self.history.append({"role": role, "parts": [{"text": content}]})

    def get(self):
        return self.history

    def clear(self):
        self.history = []