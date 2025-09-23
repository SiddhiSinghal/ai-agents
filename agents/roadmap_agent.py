# roadmap_agent.py
import json
import random

class RoadmapAgent:
    @staticmethod
    def handle(query):
        job_role = query.replace("How to become", "").replace("?", "").strip()
        # Simulated 5-step roadmap
        roadmap = {
            f"Step {i+1}": {
                "task": f"Do task {i+1} to become {job_role}",
                "weeks": 2,
                "resources": [f"Resource {i+1}-1", f"Resource {i+1}-2", f"Resource {i+1}-3"]
            } for i in range(5)
        }
        return f"Roadmap for '{job_role}':\n" + json.dumps(roadmap, indent=2)
