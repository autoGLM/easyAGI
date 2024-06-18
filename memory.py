import os
import pathlib
import time
import ujson

# Define the constant for memory folder
MEMORY_FOLDER = "./memory/"

class DialogEntry:
    def __init__(self, instruction, response):
        self.instruction = instruction
        self.response = response

def create_memory_folder():
    if not pathlib.Path(MEMORY_FOLDER).exists():
        pathlib.Path(MEMORY_FOLDER).mkdir(parents=True)

def save_conversation_memory(memory):
    # Create the folder if it doesn't exist
    create_memory_folder()

    # Generate a unique filename based on the timestamp
    timestamp = str(int(time.time()))  # Use the current timestamp as the filename
    filename = f"memory_{timestamp}.json"
    file_path = pathlib.Path(MEMORY_FOLDER).joinpath(filename)

    # Format the conversation memory as a list of dictionaries
    formatted_memory = [{"instruction": dialog[0], "response": dialog[1]} for dialog in memory]

    # Save the memory to the JSON file using ujson
    with open(file_path, "w", encoding="utf-8") as file:
        ujson.dump(formatted_memory, file, ensure_ascii=False, indent=2)

    return file_path

def load_conversation_memory():
    # Load all memory files from the memory folder
    create_memory_folder()
    memory_files = list(pathlib.Path(MEMORY_FOLDER).glob("*.json"))
    
    all_memory = []
    for file_path in memory_files:
        with open(file_path, "r", encoding="utf-8") as file:
            memory = ujson.load(file)
            all_memory.extend(memory)

    return all_memory

def delete_conversation_memory():
    # Delete all memory files in the memory folder
    create_memory_folder()
    memory_files = list(pathlib.Path(MEMORY_FOLDER).glob("*.json"))
    
    for file_path in memory_files:
        file_path.unlink()

def get_latest_memory():
    # Get the latest memory file based on the timestamp
    create_memory_folder()
    memory_files = sorted(pathlib.Path(MEMORY_FOLDER).glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    
    if not memory_files:
        return []

    latest_file = memory_files[0]
    with open(latest_file, "r", encoding="utf-8") as file:
        memory = ujson.load(file)

    return memory

