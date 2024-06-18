# SocraticReasoning.py
import logging

# Initialize logging
logging.basicConfig(filename='reasoning.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class SocraticReasoning:
    def __init__(self):
        self.premises = []
        self.logger = logging.getLogger('SocraticReasoning')
        self.logger.setLevel(logging.INFO)

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
            self.log('No premises available for drawing a conclusion.', level='error')
            return

        conclusion = "Based on the premises: "
        for premise in self.premises:
            conclusion += f"\n- {premise}"
        conclusion += "\nWe may conclude that further discussion and reasoning are needed."
        self.log(conclusion)

    def interact(self):
        while True:
            self.log("\nCommands: add, challenge, conclude, exit")
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
            else:
                self.log('Invalid command.', level='error')

if __name__ == '__main__':
    reasoner = SocraticReasoning()
    reasoner.log('SocraticReasoning initialized.')
    reasoner.interact()

