# easyAGI.py
import openai
from api import APIManager
from bdi import BDIModel, Belief, Desire, Intention
from logic import LogicTables
from SocraticReasoning import SocraticReasoning
from reasoning import Reasoning
from self_healing import SelfHealingSystem
from memory import save_conversation_memory, load_conversation_memory, delete_conversation_memory
from chatter import GPT4o, GroqModel, OllamaModel

class AGI:
    def __init__(self):
        # Initialize API Manager
        self.api_manager = APIManager()
        self.manage_api_keys()
        
        self.openai_api_key = self.api_manager.get_api_key('openai')
        self.groq_api_key = self.api_manager.get_api_key('groq')
        self.ollama_api_key = 'ollama'  # Ollama doesn't require an actual API key, just the identifier

        if self.openai_api_key and self.groq_api_key and self.ollama_api_key:
            self.chatter = self.select_provider()
        elif self.openai_api_key:
            print(f"DEBUG: Using OpenAI API key: {self.openai_api_key}")  # Debug statement
            self.chatter = GPT4o(self.openai_api_key)
        elif self.groq_api_key:
            self.chatter = GroqModel(self.groq_api_key)
        elif self.ollama_api_key:
            self.chatter = OllamaModel()
        else:
            print("No API key found for OpenAI, Groq, or Ollama.")
            self.manage_api_keys()
        
        # Initialize other components
        self.bdi_model = BDIModel()
        self.logic_tables = LogicTables()
        self.socratic_reasoner = SocraticReasoning(self.chatter)  # Pass the chatter instance
        self.reasoner = Reasoning(self.chatter)  # Pass the chatter instance
        self.self_healer = SelfHealingSystem()

    def manage_api_keys(self):
        while True:
            self.api_manager.list_api_keys()
            action = input("Choose an action: (a) Add API key, (d) Delete API key, (l) List API keys, (Press Enter to continue): ").strip().lower()
            if not action:
                self.openai_api_key = self.api_manager.get_api_key('openai')
                self.groq_api_key = self.api_manager.get_api_key('groq')
                self.ollama_api_key = 'ollama' if 'ollama' in self.api_manager.api_keys else None
                if self.openai_api_key or self.groq_api_key or self.ollama_api_key:
                    break
                else:
                    print("No API keys found. Please add at least one API key.")
            elif action == 'a':
                self.api_manager.add_api_key_interactive()
            elif action == 'd':
                api_name = input("Enter the API name to delete: ").strip()
                if api_name:
                    self.api_manager.remove_api_key(api_name)
            elif action == 'l':
                self.api_manager.list_api_keys()

    def select_provider(self):
        while True:
            choice = input("Multiple API keys found. Select the provider (1 for OpenAI, 2 for Groq, 3 for Ollama): ").strip()
            if choice == '1':
                return GPT4o(self.openai_api_key)
            elif choice == '2':
                return GroqModel(self.groq_api_key)
            elif choice == '3':
                return OllamaModel()
            else:
                print("Invalid choice. Please select 1 for OpenAI, 2 for Groq, or 3 for Ollama.")

    def perceive_environment(self):
        # This method should gather data from the environment
        agi_prompt = input("Enter the problem to solve (or type 'exit' to quit): ")
        return agi_prompt
    
    def learn_from_data(self, data):
        # This method should process and learn from the gathered data
        new_belief = Belief(data, self.chatter)
        self.bdi_model.update_beliefs({data: new_belief})
        
        new_desire = Desire(f"Solve: {data}")
        self.bdi_model.set_desires([new_desire])
        
        self.bdi_model.form_intentions()
        
        self.logic_tables.add_variable('Belief')
        self.logic_tables.add_expression('True')  # Simplified example
        truth_table = self.logic_tables.generate_truth_table()
        
        # Display truth table
        for row in truth_table:
            print("\t".join(map(str, row)))
        
        self.socratic_reasoner.add_premise(data)
        self.socratic_reasoner.draw_conclusion()

        self.reasoner.add_premise(data)
        self.reasoner.draw_conclusion()
        
        return data
    
    def make_decisions(self, knowledge):
        # This method should make decisions based on the learned knowledge
        decision = self.chatter.generate_response(knowledge)
        return decision
    
    def communicate_response(self, decisions):
        # This method should communicate the decision made
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

