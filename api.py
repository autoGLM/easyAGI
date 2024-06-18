# api.py
import os
from dotenv import load_dotenv

class APIManager:
    def __init__(self, env_file='.env'):
        self.env_file = env_file
        self.check_env_file()
        load_dotenv(self.env_file)
        self.api_keys = self.load_api_keys()

    def check_env_file(self):
        if not os.path.exists(self.env_file):
            with open(self.env_file, 'w') as f:
                f.write("# Environment variables\n")
            print(f"{self.env_file} created.")

    def load_api_keys(self):
        api_keys = {}
        for key, value in os.environ.items():
            if key.endswith('_API_KEY'):
                api_keys[key] = value
        return api_keys

    def add_api_key(self):
        print("No API keys found. Please add API keys.")
        while True:
            api_name = input("Enter API name (or press Enter to finish): ").strip()
            if not api_name:
                break
            api_key = input(f"Enter API key for {api_name}: ").strip()
            key_name = f"{api_name.upper()}_API_KEY"
            self.api_keys[key_name] = api_key
            with open(self.env_file, 'a') as f:
                f.write(f"\n{key_name}={api_key}")
            print(f"API key for {api_name} added.")

    def get_api_key(self, api_name):
        key_name = f"{api_name.upper()}_API_KEY"
        return self.api_keys.get(key_name)

    def ensure_api_keys(self):
        if not self.api_keys:
            self.add_api_key()
        else:
            print("API keys loaded successfully.")

# Usage example
if __name__ == "__main__":
    api_manager = APIManager()
    api_manager.ensure_api_keys()
    # Example of how to get an API key
    openai_api_key = api_manager.get_api_key('openai')
    if openai_api_key:
        print(f"OpenAI API key: {openai_api_key}")
    else:
        print("OpenAI API key not found.")
