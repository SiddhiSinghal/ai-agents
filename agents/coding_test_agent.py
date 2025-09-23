# coding_test_agent.py
import random

class CodingTestAgent:
    questions = [
        "Reverse a string.",
        "Check if a number is prime.",
        "Print the first n Fibonacci numbers.",
        "Find factorial of a number."
    ]
    
    @staticmethod
    def handle(query):
        question = random.choice(CodingTestAgent.questions)
        return f"Coding Question: {question}"
