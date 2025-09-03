import os
import shutil
import uuid
import json
import traceback
from src.config import FOLDER_QUEUE, FOLDER_PROCESSED, FOLDER_REJECTED
from src.database import upsert_resume

def handle_resume(filename: str, resume_str: str):
    cleaned_str = resume_str.strip().strip("```json").strip("```")

    if not cleaned_str:
        print(f"Skipping file: {filename}")
        return

    try:
        resume = json.loads(cleaned_str)
        status = resume.get("status", "invalid")

        if status == "valid":
            unique_id = str(uuid.uuid4())
            upsert_resume(unique_id, resume, filename)
            shutil.move(f"{FOLDER_QUEUE}/{filename}", f"{FOLDER_PROCESSED}/{filename}")
        else:
            shutil.move(f"{FOLDER_QUEUE}/{filename}", f"{FOLDER_REJECTED}/{filename}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON for file: {filename}")
        print(f"Invalid string content: {resume_str}")
        print(f"Error details: {e}")

    except Exception as e:
        print(f"Unexpected error for file: {filename}")
        print(f"Invalid string content: {resume_str}")
        traceback.print_exc()
