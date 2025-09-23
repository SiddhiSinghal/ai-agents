import openai, os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_career_info(career_name):
    prompt = f"""
    Provide detailed information about the career '{career_name}' in the following JSON format:
    {{
        "title": "",
        "description": "",
        "skills": [],
        "responsibilities": [],
        "education": "",
        "salary": "",
        "outlook": ""
    }}
    Make it detailed and professional.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a career guidance expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=1000
        )
        content = response['choices'][0]['message']['content']
        return json.loads(content)
    except Exception as e:
        print(e)
        return {
            "title": career_name,
            "description": "Information unavailable",
            "skills": [],
            "responsibilities": [],
            "education": "",
            "salary": "",
            "outlook": ""
        }
