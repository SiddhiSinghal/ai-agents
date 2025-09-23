# job_recommendation_agent.py
import random

class JobRecommendationAgent:
    @staticmethod
    def handle(query):
        # Simulate job recommendation based on fake scores
        jobs = ["Software Engineer", "Data Scientist", "UX Designer", "Product Manager", "ML Engineer"]
        top_jobs = random.sample(jobs, 3)
        return f"Recommended jobs based on your fake scores: {', '.join(top_jobs)}"
