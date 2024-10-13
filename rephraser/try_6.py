import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from sec import api_key

# Initialize the ChatGroq model
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=api_key
    # other params...
)

# Define the prompt for correcting sentences
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a professional resume editor. Correct the following sentence for clarity and professionalism.Dont use we ,  instead keep it like 'Developed an AI-driven portal for creating resumes tailored to specific job descriptions.' be free of first-person pronouns and provide only the rephrased sentence and no other explanation"),
        ("human", "{user_input}"),
    ]
)

# Function to correct user sentence
def correct_sentence(user_input):
    chain = prompt | llm
    message = chain.invoke(
        {
            "user_input": user_input,
        }
    )
    return message.content

# Example usage
if __name__ == "__main__":
    user_sentence = "AI based resume creation portal wrt to provided jd"
    
    corrected_sentence = correct_sentence(user_sentence)
    
   
    print(corrected_sentence)