# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# #
# def parse_resume(resume_text):
#     prompt = f"""
# You are an expert career coach. Based on the following resume text, suggest the most suitable job role title:

# Resume:
# {resume_text}

# Job Role:
# """

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are an AI resume analyzer."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.5,
#         max_tokens=50
#     )

#     return response.choices[0].message.content.strip()

# def generate_questions(role):
#     prompt = f"""
# Generate 3 technical interview questions for the role of {role}. Provide them as a numbered list.
# """

#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are an AI interview coach."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.7,
#         max_tokens=200
#     )

#     return response.choices[0].message.content.strip()



def parse_resume(text):
    return "Frontend Developer"

def generate_questions(role):
    return f"1. What is React?\n2. What is JSX?\n3. How do you manage state in {role}?"
