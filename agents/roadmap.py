import openai, os, json
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_roadmap(job_role, user_scores, weeks=10):
    score_summary = "\n".join([f"{k}: {v}%" for k, v in user_scores.items()])
    prompt = f"""
    You are an expert career counselor.
    The student has the following skills and subject performance:
    {score_summary}
    Generate a 5-step learning roadmap for becoming a successful '{job_role}' in {weeks} weeks.
    Each step should include:
    - Task
    - Weeks
    - 3 Recommended Resources
    Format JSON like:
    {{
        "step_1": {{"task": "", "weeks": , "resources": ["", "", ""]}},
        "step_2": {{"task": "", "weeks": , "resources": ["", "", ""]}},
        "step_3": {{"task": "", "weeks": , "resources": ["", "", ""]}},
        "step_4": {{"task": "", "weeks": , "resources": ["", "", ""]}},
        "step_5": {{"task": "", "weeks": , "resources": ["", "", ""]}}
    }}
    Ensure sum of weeks = {weeks}.
    Only return JSON.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that returns only JSON formatted learning roadmaps."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1000
        )
        return json.loads(response['choices'][0]['message']['content'])
    except Exception as e:
        print(e)
        return {}
