# creativity_test_agent.py
import random
import re

class CreativityTestAgent:
    @staticmethod
    def handle(story):
        # Simple creativity scoring
        unique_words = len(set(story.split()))
        score = min(10, unique_words // 5)
        feedback = f"Creativity Score: {score}/10"
        return feedback
