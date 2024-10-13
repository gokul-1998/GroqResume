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

# Define the prompt for correcting sentences with context
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a professional resume editor. Correct the following sentence for clarity and professionalism in the context provided.Give the output  in past tense and be free of first-person pronouns.Dont say The project"),
        ("human", "Context: {context}\nSentence: {user_input}"),
    ]
)

# Function to correct user sentence with context
def correct_sentence(user_input, context):
    chain = prompt | llm
    message = chain.invoke(
        {
            "user_input": user_input,
            "context": context
        }
    )
    return message.content

# Example usage
if __name__ == "__main__":
    user_sentence = "AI based resume creation portal wrt to provided jd"
    context = "This project focuses on developing a tool that generates resumes tailored to specific job descriptions."

    corrected_sentence = correct_sentence(user_sentence, context)
    
    print(corrected_sentence)
