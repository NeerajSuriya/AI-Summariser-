import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

FOLDER_QUEUE = "resumes/queue"
FOLDER_PROCESSED = "resumes/processed"
FOLDER_REJECTED = "resumes/rejected"
