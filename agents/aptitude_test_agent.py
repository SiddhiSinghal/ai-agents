# aptitude_test_agent.py
import random

class AptitudeTestAgent:
    questions = [
        "What is 15 + 27?",
        "If a train runs 60 km in 1.5 hours, what is its speed?",
        "Solve: 12 * 8 - 5",
        "What comes next in series: 2, 4, 8, 16, ?"
    ]
    
    @staticmethod
    def handle(query):
        question = random.choice(AptitudeTestAgent.questions)
        return f"Aptitude Question: {question}"
