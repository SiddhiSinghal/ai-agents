# agents/coding_agent.py
class CodingAgent:
    def run(self, code):
        # simple evaluator: count keywords
        score = 0
        if "for" in code or "while" in code:
            score += 2
        if "if" in code:
            score += 2
        if "return" in code:
            score += 2
        return {"feedback": f"Coding Score: {score}/6"}
