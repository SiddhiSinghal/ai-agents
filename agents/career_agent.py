# agents/career_agent.py
class CareerAgent:
    def run(self, job_role):
        if job_role == "Data Scientist":
            return ["Learn Python", "Master ML", "Do Kaggle projects", "Build portfolio"]
        elif job_role == "Software Engineer":
            return ["Learn DSA", "System Design", "Open Source contributions"]
        else:
            return ["Explore fundamentals", "Pick specialization", "Internships"]
