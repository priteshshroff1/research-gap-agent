import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# # Initialize Gemini model
# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.5-flash",
#     google_api_key=os.getenv("GEMINI_API_KEY"),
#     temperature=0.2
# )

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)
def generate(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the generated text.
    """

    response = llm.invoke(prompt)

    return response.content