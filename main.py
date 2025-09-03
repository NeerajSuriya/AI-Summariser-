import os
from src.config import FOLDER_QUEUE
from src.extractor import extract_text_from_pdf
from src.summariser import summarise_resume
from src.file_handler import handle_resume
from src.watcher import start_watcher


def process_queue(filepath: str):
        filename = os.path.basename(filepath)
        if filename.lower().endswith(".pdf"):
            print(f"Processing file: {filename}")
            text = extract_text_from_pdf(filepath)
            summary_json = summarise_resume(text)
            handle_resume(filename, summary_json)
            print(f"Finished processing file: {filename}")

FOLDER_QUEUE = "resumes/queue"

def process_existing_files():
    for filename in os.listdir(FOLDER_QUEUE):
        filepath = os.path.join(FOLDER_QUEUE, filename)
        if filename.lower().endswith(".pdf"):
            process_queue(filepath)

if __name__ == "__main__":
    process_existing_files()
    start_watcher(process_queue)
