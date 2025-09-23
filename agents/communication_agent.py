# agents/communication_agent.py
class CommunicationAgent:
    def run(self, text):
        words = len(text.split())
        clarity = "Good" if words < 50 else "Verbose"
        return {"clarity": clarity, "length": words}
