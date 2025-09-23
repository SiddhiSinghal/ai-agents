# agents/creativity_agent.py
import re

class CreativityAgent:
    def run(self, story):
        score = (self.creativity(story) + self.coherence(story) + (10 - self.grammar(story)) + self.engagement(story)) / 4
        return {"feedback": f"Story Score: {score:.2f}/10"}

    def grammar(self, story):
        return len(re.findall(r'\b(is|are|was|were)\s+a\b', story, re.IGNORECASE))

    def creativity(self, story):
        return min(10, len(set(story.split())) // 10)

    def coherence(self, story):
        sentences = re.split(r'[.!?]', story)
        return min(10, len(set(sentences)) // 5)

    def engagement(self, story):
        words = len(story.split())
        sentences = re.split(r'[.!?]', story)
        return min(10, (words + len(set(sentences))) // 20)
