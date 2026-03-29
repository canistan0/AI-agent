from agent import Agent
from memory import MemoryManager

def main():
    memory = MemoryManager()
    agent = Agent(memory)

    print("AI Agent Ready. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = agent.run(user_input)
        print(f"Agent: {response}\n")

if __name__ == "__main__":
    main()