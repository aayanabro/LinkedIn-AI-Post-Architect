import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"), 
    model_name="llama-3.3-70b-versatile"
)

if __name__ == "__main__":
    response = llm.invoke("What are the 2 main ingredients in a samosa?")
    print(response.content)