# chatter.py
import openai
from groq import Groq
import logging

class GPT4o:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key

    def generate_response(self, knowledge, model="gpt-4o"):
        prompt = f"{knowledge}"
        try:
            response = openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": ""},
                    {"role": "user", "content": prompt}
                ]
            )
            decision = response.choices[0].message.content
            return decision.lower()
        except openai.APIError as e:
            logging.error(f"openai api error: {e}")
            return "error: unable to generate a response due to an issue with the openai api."

class GroqModel:
    def __init__(self, groq_api_key):
        self.client = Groq(api_key=groq_api_key)

    def generate_response(self, knowledge, model="mixtral-8x7b-32768"):
        prompt = f"{knowledge}"
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": ""},
                    {"role": "user", "content": prompt}
                ],
                model=model,
            )
            decision = chat_completion.choices[0].message.content
            return decision.lower()
        except Exception as e:
            logging.error(f"groq api error: {e}")
            return "error: unable to generate a response due to an issue with the groq api."

class OllamaModel:
    def __init__(self):
        self.client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama',  # required, but unused
        )

    def generate_response(self, knowledge, model="llama2"):
        prompt = [
            {"role": "system", "content": ""},
            {"role": "assistant", "content": ""},
            {"role": "tool", "content": ""},
            {"role": "user", "content": f"{knowledge}"}
        ]
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=prompt
            )
            decision = response.choices[0].message.content
            return decision.lower()
        except Exception as e:
            logging.error(f"ollama api error: {e}")
            return "error: unable to generate a response due to an issue with the ollama api."

