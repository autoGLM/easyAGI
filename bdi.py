# bdi.py
class Belief:
    def __init__(self, statement):
        self.statement = statement

class Desire:
    def __init__(self, goal):
        self.goal = goal

class Intention:
    def __init__(self, action):
        self.action = action

class BDIModel:
    def __init__(self):
        self.beliefs = []
        self.desires = []
        self.intentions = []

    def add_belief(self, belief):
        self.beliefs.append(belief)

    def add_desire(self, desire):
        self.desires.append(desire)

    def add_intention(self, intention):
        self.intentions.append(intention)

    def process_bdi(self):
        # Simplified BDI processing
        for belief in self.beliefs:
            print(f"Processing belief: {belief.statement}")
        for desire in self.desires:
            print(f"Processing desire: {desire.goal}")
        for intention in self.intentions:
            print(f"Processing intention: {intention.action}")
