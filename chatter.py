# chatter.py
import os
import openai
from groq import Groq
from openai import OpenAI

class GPT4o:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key

    def generate_response(self, knowledge, model="gpt-4"):
        prompt = f"Autonomous general intelligence return solution: {knowledge}."
        
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are openmind the easy action event AGI solution creator."},
                {"role": "user", "content": prompt}
            ]
        )
        decision = response.choices[0].message['content']
        return decision

class GroqModel:
    def __init__(self, groq_api_key):
        self.client = Groq(api_key=groq_api_key)

    def generate_response(self, knowledge, model="mixtral-8x7b-32768"):
        prompt = f"Autonomous general intelligence return solution: {knowledge}."
        
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are openmind the easy action event AGI solution creator."},
                {"role": "user", "content": prompt}
            ],
            model=model,
        )
        
        decision = chat_completion.choices[0].message.content
        return decision

class OllamaModel:
    def __init__(self):
        self.client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama',  # required, but unused
        )

    def generate_response(self, knowledge, model="llama2"):
        prompt = [
            {"role": "mastermind", "content": "controller of agency"},
            {"role": "SimpleCoder", "content": "terminal interaction with bash, python and more"},
            {"role": "autoGLM", "content": "autonomous general learning model"},
            {"role": "codephreak", "content": "Software Engineer Systems Architect"},
            {"role": "user", "content": f"Autonomous general intelligence return solution: {knowledge}."}
        ]
        
        response = self.client.chat.completions.create(
            model=model,
            messages=prompt
        )
        
        decision = response.choices[0].message.content
        return decision

