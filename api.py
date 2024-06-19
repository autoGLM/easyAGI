# api.py
import os
from dotenv import load_dotenv, set_key, unset_key, dotenv_values

class APIManager:
    def __init__(self, env_file='.env'):
        self.env_file = env_file
        load_dotenv(self.env_file)
        self.api_keys = self.load_api_keys()

    def load_api_keys(self):
        api_keys = {}
        for key, value in dotenv_values(self.env_file).items():
            if key.endswith('_API_KEY'):
                api_keys[key] = value
        return api_keys

    def get_api_key(self, api_name):
        key_name = f"{api_name.upper()}_API_KEY"
        api_key = self.api_keys.get(key_name)
        print(f"DEBUG: Loaded API key for {api_name}: {api_key}")  # Debug statement
        return api_key

    def add_api_key_interactive(self):
        while True:
            api_name = input("Enter API name (or press Enter to quit): ").strip()
            if not api_name:
                break
            api_key = input(f"Enter API key for {api_name}: ").strip()
            if not api_key:
                print("API key cannot be empty.")
                continue
            key_name = f"{api_name.upper()}_API_KEY"
            self.api_keys[key_name] = api_key
            set_key(self.env_file, key_name, api_key)
            print(f"API key for {api_name} added.")

    def list_api_keys(self):
        print("Loaded API keys:")
        for key in self.api_keys.keys():
            api_name = key.replace('_API_KEY', '').lower()
            print(f"- {api_name}")

    def remove_api_key(self, api_name):
        key_name = f"{api_name.upper()}_API_KEY"
        if key_name in self.api_keys:
            unset_key(self.env_file, key_name)
            del self.api_keys[key_name]
            print(f"API key for {api_name} removed.")
        else:
            print(f"No API key found for {api_name}.")

# Usage example
if __name__ == "__main__":
    api_manager = APIManager()
    openai_api_key = api_manager.get_api_key('openai')
    if openai_api_key:
        print(f"OpenAI API key: {openai_api_key}")
    else:
        print("OpenAI API key not found.")
