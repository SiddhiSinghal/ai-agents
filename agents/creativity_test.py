import re

PROMPTS = [
    "Write a story about a world where dreams come true.",
    "Describe a day in the life of a time traveler.",
    "A mysterious door appears in your house. What happens next?",
    "You wake up with a superpower. How do you use it?"
]

def get_prompt():
    import random
    return random.choice(PROMPTS)

def assess_creativity(story):
    unique_words = set(story.split())
    return min(10, len(unique_words)//10)

def check_grammar(story):
    return len(re.findall(r'\b(is|are|was|were)\s+a\b', story, re.IGNORECASE))

def assess_coherence(story):
    sentences = re.split(r'[.!?]', story)
    return min(10, len(set(sentences))//5)

def assess_engagement(story):
    sentences = re.split(r'[.!?]', story)
    return min(10, (len(story.split())+len(set(sentences)))//20)

def get_feedback(story):
    score = (assess_creativity(story)+assess_coherence(story)+(10-check_grammar(story))+assess_engagement(story))/4
    return f"Overall Score: {score:.2f}/10", score
