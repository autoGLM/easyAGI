# bdi.py
from reasoning import Reasoning

class Belief:
    def __init__(self, data, chatter):
        self.data = data
        self.reasoning = Reasoning(chatter)  # Initialize Reasoning class with the chatter instance
        # Perform reasoning on the belief data
        self.conclusion = self.reasoning.draw_conclusion()

class Desire:
    def __init__(self, goal):
        self.goal = goal

class Intention:
    def __init__(self, plan):
        self.plan = plan

class BDIModel:
    def __init__(self):
        self.beliefs = {}
        self.desires = []
        self.intentions = []

    def update_beliefs(self, new_beliefs):
        self.beliefs.update(new_beliefs)

    def set_desires(self, new_desires):
        self.desires = new_desires

    def form_intentions(self):
        # Form intentions based on beliefs and desires
        for desire in self.desires:
            plan = f"Plan to achieve: {desire.goal}"
            self.intentions.append(Intention(plan))

