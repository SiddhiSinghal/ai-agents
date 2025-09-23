# orchestrator.py
import sys
import os

# Add agents folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), "agents"))

# Import agents
from career_exploration_agent import CareerExplorationAgent
from roadmap_agent import RoadmapAgent
from job_recommendation_agent import JobRecommendationAgent
from coding_test_agent import CodingTestAgent
from aptitude_test_agent import AptitudeTestAgent
from creativity_test_agent import CreativityTestAgent
from communication_test_agent import CommunicationTestAgent

def route_query(query):
    query_lower = query.lower()
    
    if "tell me about" in query_lower:
        return CareerExplorationAgent.handle(query)
    elif "how to become" in query_lower:
        return RoadmapAgent.handle(query)
    elif "suggest job" in query_lower:
        return JobRecommendationAgent.handle(query)
    elif "coding question" in query_lower:
        return CodingTestAgent.handle(query)
    elif "aptitude question" in query_lower:
        return AptitudeTestAgent.handle(query)
    elif "creativity test:" in query_lower:
        story = query.split("creativity test:")[1].strip()
        return CreativityTestAgent.handle(story)
    elif "communication test:" in query_lower:
        response = query.split("communication test:")[1].strip()
        return CommunicationTestAgent.handle(response)
    else:
        return "Sorry, I couldn't understand. Please rephrase."

def main():
    print("Welcome to the Multi-Agent Career Guidance System!")
    print("Type 'exit' to quit.")
    while True:
        query = input("\nYou: ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        response = route_query(query)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()
