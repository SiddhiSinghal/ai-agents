# orchestrator.py
from agents.auth_agent import AuthAgent
from agents.db_agent import DBAgent
from agents.job_agent import JobPredictionAgent
from agents.aptitude_agent import AptitudeAgent
from agents.coding_agent import CodingAgent
from agents.creativity_agent import CreativityAgent
from agents.communication_agent import CommunicationAgent
from agents.industry_agent import IndustryAgent
from agents.career_agent import CareerAgent

class Orchestrator:
    def __init__(self):
        self.agents = {
            "auth": AuthAgent(),
            "db": DBAgent(),
            "job": JobPredictionAgent(),
            "aptitude": AptitudeAgent(),
            "coding": CodingAgent(),
            "creativity": CreativityAgent(),
            "communication": CommunicationAgent(),
            "industry": IndustryAgent(),
            "career": CareerAgent()
        }

    def handle(self, agent_name, query):
        if agent_name not in self.agents:
            return f"❌ Unknown agent: {agent_name}"
        return self.agents[agent_name].run(query)
