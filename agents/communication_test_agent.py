# communication_test_agent.py
import re

class CommunicationTestAgent:
    @staticmethod
    def handle(response):
        # Simple communication scoring
        length = len(response.split())
        sentences = len(re.split(r'[.!?]', response))
        score = min(10, (length + sentences) // 10)
        feedback = f"Communication Score: {score}/10"
        return feedback
