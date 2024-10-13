import datetime
from langchain_core.prompts import ChatPromptTemplate

from langchain_groq import ChatGroq
from sec import api_key
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=api_key
    # other params...
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "{ai_system}",
        ),
        ("human", "{user_input}"),
    ]
)

with open('resume.txt', 'r') as resume_file:
    resume = resume_file.read()

with open('jobDescription.txt', 'r') as job_description_file:
    jobDescription = job_description_file.read()

chain = prompt | llm
message=chain.invoke(
    {
        
        "user_input":  "Build a custom resume for this job posting here is the resume:" + resume + "  and here is the job description " + jobDescription,
        "ai_system": "Please provide the job posting details, and I'll create a custom resume tailored to the job requirements.\n\nPlease provide the following information:\n\n1. Job title\n2. Job description\n3. Requirements (e.g., skills, experience, education)\n4. Any specific keywords or phrases mentioned in the job posting\n\nOnce I have this information, I'll create a custom resume that highlights your relevant skills and experiences, increasing your chances of getting noticed by the hiring manager.",
    }
)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
output_file_name = f"resume_{timestamp}.md"    

with open(output_file_name, 'w') as output_file:
    output_file.write(message.content)
