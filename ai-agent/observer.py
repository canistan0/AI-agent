
class LoggerObserver:
    def update(self, event: str, data: str):
        print(f"[LOG] {event}: {data}")