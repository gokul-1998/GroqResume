from groq import Groq
from sec import api_key
client = Groq(
    api_key=api_key
)

with open('resume.txt', 'r') as resume_file:
    resume = resume_file.read()

with open('jobDescription.txt', 'r') as job_description_file:
    jobDescription = job_description_file.read()


messages=[
        {
            "role": "user",
            "content": "Build a custom resume for this job posting here is the resume:" + resume + "  and here is the job description " + jobDescription
        },
        {
            "role": "assistant",
            "content": "Please provide the job posting details, and I'll create a custom resume tailored to the job requirements.\n\nPlease provide the following information:\n\n1. Job title\n2. Job description\n3. Requirements (e.g., skills, experience, education)\n4. Any specific keywords or phrases mentioned in the job posting\n\nOnce I have this information, I'll create a custom resume that highlights your relevant skills and experiences, increasing your chances of getting noticed by the hiring manager."
        }
    ]

# print(messages)

completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=messages,
    temperature=1,                                                                                                                                  
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion)
print(completion.choices[0].message.content)
