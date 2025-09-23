# orchestrator.py
import sys
from agents import (
    career_exploration,
    roadmap,
    job_recommendation,
    coding_test,
    aptitude_test,
    creativity_test,
    communication_test
)

def main():
    print("Welcome to the Career Guidance Multi-Agent System!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Decide which agent to call based on keywords
        if "career" in user_input or "explore" in user_input:
            career_name = input("Enter the career you want info on: ")
            info = career_exploration.get_career_info(career_name)
            print("\nCareer Exploration Result:")
            print(info)

        elif "roadmap" in user_input or "plan" in user_input:
            job_role = input("Enter the job role you want a roadmap for: ")
            weeks = input("How many weeks to complete? (default 10): ")
            weeks = int(weeks) if weeks.isdigit() else 10
            user_scores = {}  # Fake or random scores for demo
            for field in ['DSA','DBMS','OS','CN','Mathmetics','Aptitute','Comm','Problem_Solving','Creative','Hackathons']:
                user_scores[field] = 50  # Example: 50% in everything
            roadmap_data = roadmap.get_roadmap(job_role, user_scores, weeks)
            print("\nRoadmap:")
            for step, details in roadmap_data.items():
                print(f"{step}: {details}")

        elif "job" in user_input or "recommendation" in user_input:
            print("Simulating Job Recommendation based on fake scores...")
            user_data = [50]*10
            top_jobs = job_recommendation.predict_jobs(user_data)
            print("Top Recommended Jobs:", top_jobs)

        elif "coding" in user_input or "programming" in user_input:
            question = coding_test.get_random_question()
            print("Coding Question:", question)
            code = input("Enter your solution (or skip): ")
            if code.strip():
                output, marks = coding_test.evaluate_code(code, question)
                print(f"Output:\n{output}\nMarks: {marks}")

        elif "aptitude" in user_input or "quiz" in user_input:
            questions = aptitude_test.get_random_questions()
            score = 0
            for q in questions:
                ans = input(f"{q['question']} = ")
                if ans.strip() == q['answer']:
                    score += 10
            print(f"Aptitude Test Score: {score}/{len(questions)*10}")

        elif "creativity" in user_input or "story" in user_input:
            prompt = creativity_test.get_prompt()
            print("Story Prompt:", prompt)
            story = input("Write your story: ")
            feedback, score = creativity_test.get_feedback(story)
            print(f"Creativity Test Feedback: {feedback}")

        elif "communication" in user_input or "text" in user_input:
            text = input("Enter a sample text to assess: ")
            feedback, score = communication_test.assess_communication(text)
            print(f"Communication Test Feedback: {feedback}")

        else:
            print("Sorry, I couldn't understand. Try keywords like 'career', 'roadmap', 'job', 'coding', 'aptitude', 'creativity', 'communication'.")

if __name__ == "__main__":
    main()
