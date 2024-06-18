# easyAGI (c) Gregory L. Magnusson GPLv3 license 2024
# easyAGI.py
import openai
from api import APIManager

# Initialize API Manager and ensure API keys are available
api_manager = APIManager()
api_manager.ensure_api_keys()

# Set the OpenAI API key from the loaded API keys
openai_api_key = api_manager.get_api_key('openai')
if openai_api_key:
    openai.api_key = openai_api_key
else:
    print("OpenAI API key not found. Exiting...")
    exit(1)

def get_solution_from_agi(agi_prompt):
    prompt = f"Autonomous general intelligence return solution: {agi_prompt}."

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are openmind the easy action event AGI solution creator."},
            {"role": "user", "content": prompt}
        ]
    )
    solution = response.choices[0].message['content']
    return solution

def main():
    while True:
        agi_prompt = input("Enter the problem to solve (or type 'exit' to quit): ")
        if agi_prompt.lower() == 'exit':
            break
        solution = get_solution_from_agi(agi_prompt)
        print(f"\nSolution:\n{solution}\n")

if __name__ == "__main__":
    main()
