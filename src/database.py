from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from src.config import PINECONE_API_KEY

pc = Pinecone(api_key=PINECONE_API_KEY)

INDEX_NAME = "resumes"
if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)
hf_model = SentenceTransformer("all-MiniLM-L6-v2")

def upsert_resume(unique_id, resume: dict, filename: str):
    text_to_embed = resume["summary"] + " Skills: " + str(resume["skills"])
    embedding = hf_model.encode(text_to_embed).tolist()

    metadata = {
        "name": resume["name"],
        "email": resume["email"],
        "phone": resume["phone"],
        "location": resume["location"],
        "skills": str(resume["skills"]),
        "summary": resume["summary"],
        "filename": filename
    }

    index.upsert([{
        "id": unique_id,
        "values": embedding,
        "metadata": metadata
    }])
