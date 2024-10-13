import datetime
from groq import Groq
from sec import api_key
client = Groq(
        api_key=api_key

)
with open('resume.txt', 'r') as resume_file:
    resume = resume_file.read()

with open('jobDescription.txt', 'r') as job_description_file:
    jobDescription = job_description_file.read()

messages = [
    {
        "role": "user",
        "content": f"Build a custom resume for this job posting here is the resume: {resume} and here is the job description: {jobDescription}"
    }
]

# Create the chat completion
completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=messages,
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,  # Set to False if streaming doesn't work
    stop=None,
)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
output_file_name = f"resume_{timestamp}.md"   
# Open the output file in write mode
with open(output_file_name, 'w') as output_file:
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end="")
            output_file.write(content)
        else:
            print("Received empty chunk.")
