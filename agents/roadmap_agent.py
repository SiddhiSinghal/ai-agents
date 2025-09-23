class RoadmapAgent:
    def generate(self, job_role):
        if job_role == "Data Scientist":
            return ["Learn Python", "Master ML", "Build projects"]
        elif job_role == "Software Engineer":
            return ["Master DSA", "Learn System Design", "Contribute to open source"]
        else:
            return ["Explore fundamentals", "Build portfolio projects"]
