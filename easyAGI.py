# easyAGI.py
# openmind (c) Gregory L. Magnusson 2024 MIT license
import openai
from api import APIManager
from bdi import BDIModel, Belief, Desire, Intention
from logic import LogicTables
from SocraticReasoning import SocraticReasoning
from reasoning import Reasoning
from self_healing import SelfHealing
from memory import save_conversation_memory, load_conversation_memory, delete_conversation_memory, get_latest_memory

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

# Initialize BDI Model, Logic Tables, Socratic Reasoning, Reasoning, and Self Healing
bdi_model = BDIModel()
logic_tables = LogicTables()
socratic_reasoner = SocraticReasoning()
reasoner = Reasoning()
self_healer = SelfHealing()

# Initialize conversation memory
conversation_memory = []

def get_solution_from_agi(agi_prompt):
    prompt = f"Autonomous general intelligence return solution: {agi_prompt}."

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are openmind the easy action event AGI solution creator."},
            {"role": "user", "content": prompt}
        ]
    )
    solution = response.choices[0].message.content
    return solution

def main():
    global conversation_memory

    while True:
        agi_prompt = input("Enter the problem to solve (or type 'exit' to quit, 'load' to load memory, 'delete' to delete memory): ")
        if agi_prompt.lower() == 'exit':
            save_conversation_memory(conversation_memory)
            break
        elif agi_prompt.lower() == 'load':
            conversation_memory = load_conversation_memory()
            for entry in conversation_memory:
                print(f"Instruction: {entry['instruction']}\nResponse: {entry['response']}\n")
            continue
        elif agi_prompt.lower() == 'delete':
            delete_conversation_memory()
            conversation_memory = []
            print("Memory deleted.")
            continue

        # Update beliefs with the new prompt
        new_belief = Belief(agi_prompt)
        bdi_model.update_beliefs({agi_prompt: new_belief})
        
        # Set desires based on the new belief
        new_desire = Desire(f"Solve: {agi_prompt}")
        bdi_model.set_desires([new_desire])
        
        # Form intentions based on beliefs and desires
        bdi_model.form_intentions()
        
        # Utilize logic tables for enhanced reasoning
        logic_tables.add_variable('Belief')
        logic_tables.add_expression('True')  # Simplified example
        logic_tables.display_truth_table()
        
        # Add premises for Socratic reasoning
        socratic_reasoner.add_premise(agi_prompt)
        socratic_reasoner.draw_conclusion()

        # Add premises for general reasoning
        reasoner.add_premise(agi_prompt)
        reasoner.draw_conclusion()
        
        # Get solution from AGI
        solution = get_solution_from_agi(agi_prompt)
        print(f"\nSolution:\n{solution}\n")

        # Save the dialogue to memory
        conversation_memory.append((agi_prompt, solution))

if __name__ == "__main__":
    main()

