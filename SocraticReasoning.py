# SocraticReasoning.py
import logging
from chatter import GPT4o, GroqModel, OllamaModel

class SocraticReasoning:
    def __init__(self, chatter):
        self.premises = []
        self.logger = logging.getLogger('SocraticReasoning')
        self.logger.setLevel(logging.INFO)
        self.max_tokens = 100
        self.chatter = chatter

    def log(self, message, level='info'):
        if level == 'info':
            self.logger.info(message)
        elif level == 'error':
            self.logger.error(message)
        print(message)

    def add_premise(self, premise):
        self.premises.append(premise)
        self.log(f'Added premise: {premise}')

    def challenge_premise(self, premise):
        if premise in self.premises:
            self.premises.remove(premise)
            self.log(f'Challenged and removed premise: {premise}')
        else:
            self.log(f'Premise not found: {premise}', level='error')

    def draw_conclusion(self):
        if not self.premises:
            self.log('No premises available for logic as conclusion.', level='error')
            return

        premise_text = "\n".join(f"- {premise}" for premise in self.premises)
        prompt = f"Based on the premises:\n{premise_text}\nProvide a logical conclusion."

        # Use the appropriate model to generate the response
        conclusion = self.chatter.generate_response(prompt)
        self.log(f"Conclusion:\n{conclusion}")

    def set_max_tokens(self, max_tokens):
        self.max_tokens = max_tokens
        self.log(f"Max tokens set to: {max_tokens}")

    def interact(self):
        while True:
            self.log("\nCommands: add, challenge, conclude, set_tokens, exit")
            cmd = input("> ").strip().lower()
            
            if cmd == 'exit':
                self.log('Exiting SocraticReasoning.')
                break
            elif cmd == 'add':
                premise = input("Enter the premise: ").strip()
                self.add_premise(premise)
            elif cmd == 'challenge':
                premise = input("Enter the premise to challenge: ").strip()
                self.challenge_premise(premise)
            elif cmd == 'conclude':
                self.draw_conclusion()
            elif cmd == 'set_tokens':
                tokens = input("Enter the maximum number of tokens for the conclusion: ").strip()
                if tokens.isdigit():
                    self.set_max_tokens(int(tokens))
                else:
                    self.log("Invalid number of tokens.", level='error')
            else:
                self.log('Invalid command.', level='error')

def main():
    # Replace 'your_api_key_here' with the actual API key or retrieve it as needed
    api_key = 'your_api_key_here'
    api_provider = 'openai'  # or 'groq' or 'ollama'
    chatter = GPT4o(api_key)  # or GroqModel(api_key), OllamaModel()
    reasoner = SocraticReasoning(chatter)
    reasoner.log('SocraticReasoning initialized.')
    reasoner.interact()

if __name__ == '__main__':
    main()

