# agents/aptitude_agent.py
class AptitudeAgent:
    def run(self, answers):
        correct_answers = ["A", "C", "B", "D", "A"]  # demo key
        score = sum(1 for a, b in zip(answers, correct_answers) if a == b)
        return {"score": score, "out_of": len(correct_answers)}
