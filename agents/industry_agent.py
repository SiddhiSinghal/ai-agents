# agents/industry_agent.py
class IndustryAgent:
    def run(self, topic):
        trends = {
            "AI": "AI is growing rapidly with LLMs, GenAI, and automation.",
            "Web": "Web development is moving towards full-stack JS and serverless.",
            "Cloud": "Cloud-native, DevOps, and microservices are in demand."
        }
        return trends.get(topic, "⚠️ No info on this topic.")
