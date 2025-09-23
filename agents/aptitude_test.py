import json, random

def load_questions(file_path="aptitude_questions.json"):
    with open(file_path,"r") as f:
        return json.load(f)

def get_random_questions(n=10):
    questions = load_questions()
    return random.sample(questions, n)
