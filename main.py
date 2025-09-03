import os
from src.config import FOLDER_QUEUE
from src.extractor import extract_text_from_pdf
from src.summariser import summarise_resume
from src.file_handler import handle_resume

def process_queue():
    for filename in os.listdir(FOLDER_QUEUE):
        if filename.lower().endswith(".pdf"):
            print(f"Processing file: {filename}")
            filepath = os.path.join(FOLDER_QUEUE, filename)
            text = extract_text_from_pdf(filepath)
            summary_json = summarise_resume(text)
            handle_resume(filename, summary_json)
            print(f"Finished processing file: {filename}")

if __name__ == "__main__":
    process_queue()
