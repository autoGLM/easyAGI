# easyAGI.py
# openmind (c) Gregory L. Magnusson 2024 MIT license
import openai
from api import APIManager
from bdi import BDIModel, Belief, Desire, Intention
from logic import LogicTables
from SocraticReasoning import SocraticReasoning
from reasoning import Reasoning
from self_healing import SelfHealingSystem
from memory import save_conversation_memory, load_conversation_memory, delete_conversation_memory

class AGI:
    def __init__(self):
        # Initialize components
        self.api_manager = APIManager()
        self.api_manager.ensure_api_keys()
        self.openai_api_key = self.api_manager.get_api_key('openai')
        
        if self.openai_api_key:
            openai.api_key = self.openai_api_key
        else:
            print("OpenAI API key not found. Exiting...")
            exit(1)
        
        self.bdi_model = BDIModel()
        self.logic_tables = LogicTables()
        self.socratic_reasoner = SocraticReasoning()
        self.reasoner = Reasoning()
        self.self_healer = SelfHealingSystem()

    def perceive_environment(self):
        # This method should gather data from the environment
        agi_prompt = input("Enter the problem to solve (or type 'exit' to quit): ")
        return agi_prompt
    
    def learn_from_data(self, data):
        # This method should process and learn from the gathered data
        new_belief = Belief(data)
        self.bdi_model.update_beliefs({data: new_belief})
        
        new_desire = Desire(f"Solve: {data}")
        self.bdi_model.set_desires([new_desire])
        
        self.bdi_model.form_intentions()
        
        self.logic_tables.add_variable('Belief')
        self.logic_tables.add_expression('True')  # Simplified example
        self.logic_tables.display_truth_table()
        
        self.socratic_reasoner.add_premise(data)
        self.socratic_reasoner.draw_conclusion()

        self.reasoner.add_premise(data)
        self.reasoner.draw_conclusion()
        
        return data
    
    def make_decisions(self, knowledge):
        # This method should make decisions based on the learned knowledge
        prompt = f"Autonomous general intelligence return solution: {knowledge}."
        
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are openmind the easy action event AGI solution creator."},
                {"role": "user", "content": prompt}
            ]
        )
        decision = response.choices[0].message.content
        return decision
    
    def communicate_response(self, decisions):
        # This method should communicate the decisions made
        print(f"\nSolution:\n{decisions}\n")
    
    def main_loop(self):
        # Main loop to continuously perceive, learn, decide, and communicate
        conversation_memory = []
        while True:
            environment_data = self.perceive_environment()
            if environment_data.lower() == 'exit':
                save_conversation_memory(conversation_memory)
                break

            learned_knowledge = self.learn_from_data(environment_data)
            decisions = self.make_decisions(learned_knowledge)
            self.communicate_response(decisions)

            # Save the dialogue to memory
            conversation_memory.append((environment_data, decisions))

def main():
    agi = AGI()
    agi.main_loop()
    
if __name__ == "__main__":
    main()

