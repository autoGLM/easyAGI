import os
from dotenv import load_dotenv, set_key, unset_key, dotenv_values
from dotenv.main import DotEnv

class APIManager:
    def __init__(self, env_file='.env'):
        self.env_file = env_file
        self.dotenv = DotEnv(self.env_file)
        load_dotenv(self.env_file)
        self.api_keys = self.load_api_keys()

    def load_api_keys(self):
        api_keys = {}
        for key, value in dotenv_values(self.env_file).items():
            if key.endswith('_API_KEY'):
                api_keys[key] = value
        return api_keys

    def add_api_key(self):
        while True:
            api_name = input("Enter API name (or press r to remove an API key, or press Enter to continue): ").strip()
            if not api_name:
                break
            if api_name.lower() == 'r':
                self.list_api_keys()
                api_name_to_remove = input("Enter the API name to remove: ").strip()
                if api_name_to_remove:
                    self.remove_api_key(api_name_to_remove)
                continue
            api_key = input(f"Enter API key for {api_name}: ").strip()
            if not api_key:
                print("API key cannot be empty.")
                continue
            key_name = f"{api_name.upper()}_API_KEY"
            self.api_keys[key_name] = api_key
            set_key(self.env_file, key_name, api_key)
            print(f"API key for {api_name} added.")

    def get_api_key(self, api_name):
        key_name = f"{api_name.upper()}_API_KEY"
        return self.api_keys.get(key_name)

    def remove_api_key(self, api_name):
        key_name = f"{api_name.upper()}_API_KEY"
        if key_name in self.api_keys:
            unset_key(self.env_file, key_name)
            del self.api_keys[key_name]
            print(f"API key for {api_name} removed.")
        else:
            print(f"No API key found for {api_name}.")

    def list_api_keys(self):
        print("Loaded API keys:")
        for key in self.api_keys.keys():
            api_name = key.replace('_API_KEY', '').lower()
            print(f"- {api_name}")

    def ensure_api_keys(self):
        if not self.api_keys:
            self.add_api_key()
        else:
            self.list_api_keys()

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
    
    # Example of how to remove an API key
    api_manager.remove_api_key('openai')
    api_manager.list_api_keys()
