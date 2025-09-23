# agents/job_agent.py
class JobPredictionAgent:
    def run(self, marks):
        # very simple logic (replace with ML later)
        if marks.get("ML", 0) > 80:
            return ["Data Scientist", "AI Engineer", "ML Engineer"]
        elif marks.get("DSA", 0) > 75:
            return ["Software Engineer", "Backend Developer", "SDE-1"]
        else:
            return ["Generalist", "QA Engineer", "Support Engineer"]
