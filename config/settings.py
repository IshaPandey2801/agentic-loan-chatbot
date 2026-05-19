from crewai import LLM
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Groq LLM
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)