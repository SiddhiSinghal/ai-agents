import subprocess, random

questions = [
    "Reverse a string.",
    "Check if a number is a prime number.",
    "Find factorial of a number.",
    "Check if a number is palindrome."
]

expected_outputs = {
    "Reverse a string.": "gnirts",
    "Check if a number is a prime number.": "Prime",
    "Find factorial of a number.": "120",
    "Check if a number is palindrome.": "Palindrome"
}

def get_random_question():
    question = random.choice(questions)
    return question

def evaluate_code(user_code, question, custom_input=""):
    output, marks = "", 0
    try:
        with open("user_code.cpp","w") as f:
            f.write(user_code)

        compile_result = subprocess.run(["g++","user_code.cpp","-o","user_code.out"], capture_output=True, text=True)
        if compile_result.returncode !=0:
            output = compile_result.stderr
        else:
            run_result = subprocess.run(["./user_code.out"], input=custom_input.strip(), capture_output=True, text=True, timeout=5)
            output = run_result.stdout.strip()
            if output == expected_outputs.get(question,""):
                marks=100
            else:
                marks=50
    except subprocess.TimeoutExpired:
        output="Time Limit Exceeded"
    except Exception as e:
        output=str(e)
    return output, marks
