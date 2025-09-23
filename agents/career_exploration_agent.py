# career_exploration_agent.py

class CareerExplorationAgent:
    @staticmethod
    def handle(query):
        career_name = query.replace("Tell me about", "").strip()
        return f"Career info for '{career_name}': (simulated) You need skills X, Y, Z."
