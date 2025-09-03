from groq import Groq
from src.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def summarise_resume(text: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system",
             "content": (
                 "You are an AI assistant that extracts resume information from a resume. "
                 "Always return JSON, don’t include any other text."
             )},
            {"role": "user",
             "content": (
                 "First check if the PDF is valid or not and mark the status as valid or invalid. "
                 "If invalid, you don’t have to extract details, just return the status. "
                 f"Here is the resume:\n\n{text}\n\n"
                 "Return JSON in this format:\n"
                 "{\n"
                 '  "status": "valid" or "invalid",\n'
                 '  "name": "",\n'
                 '  "email": "",\n'
                 '  "phone": "",\n'
                 '  "location": "",\n'
                 '  "education": [],\n'
                 '  "experience": [],\n'
                 '  "skills": [],\n'
                 '  "summary": ""\n'
                 "}"
             )}
        ],
        temperature=0.0,
        max_tokens=500,
    )
    return response.choices[0].message.content
