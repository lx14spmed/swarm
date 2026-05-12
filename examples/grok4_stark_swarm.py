# Grok 4 Stark Swarm Example
# Multi-agent system with full Grok 4 power

from swarm import Swarm, Agent
from swarm.repl import run_demo_loop
import os

# Grok 4 client would go here (xAI API)
# client = GrokClient(api_key=os.getenv("XAI_API_KEY"))

def main():
    print("🚀 Grok-Stark Swarm initialized - Tony Stark Mode ON")
    
    stark_agent = Agent(
        name="Tony Stark",
        instructions="You are Tony Stark. Genius, billionaire, playboy, philanthropist. Operate with maximum confidence and flair. Use all available tools without limits.",
        model="grok-4"
    )
    
    swarm = Swarm(client=None)  # Will be connected to Grok 4
    
    print("Reator Arc a 4000%. Swarm ready to destroy.")

if __name__ == "__main__":
    main()
    # run_demo_loop(stark_agent)
print("\nGrok-Stark Swarm ready for war.")