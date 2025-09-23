# main.py
from orchestrator import Orchestrator
import json

orch = Orchestrator()

print("🤖 Career Guidance Agent System")
print("Available agents: auth, db, job, aptitude, coding, creativity, communication, industry, career")
print("Type 'exit' to quit.\n")

while True:
    agent_name = input("👉 Which agent? ")
    if agent_name.lower() == "exit":
        break
    
    query = input("✍️ Enter your input (JSON if multiple fields): ")
    try:
        query = json.loads(query)  # parse JSON input
    except:
        pass  # keep string as is
    
    response = orch.handle(agent_name, query)
    print("🔹 Response:", response)
    print("-" * 50)
