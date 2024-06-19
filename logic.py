import itertools
import json
import os
import time

class LogicTables:
    def __init__(self):
        self.variables = set()
        self.expressions = []
        self.memory_folder = "./memory/"
        self.memory_file = os.path.join(self.memory_folder, "truths.json")
        self.create_memory_folder()

    def create_memory_folder(self):
        if not os.path.exists(self.memory_folder):
            os.makedirs(self.memory_folder)

    def add_variable(self, variable):
        self.variables.add(variable)
        self.save_to_memory()

    def add_expression(self, expression):
        self.expressions.append(expression)
        self.save_to_memory()

    def evaluate_expression(self, expression, values):
        for var, val in values.items():
            expression = expression.replace(var, str(val))
        return eval(expression)

    def generate_truth_table(self):
        if not self.variables or not self.expressions:
            return "No variables or expressions to evaluate."

        headers = list(self.variables) + self.expressions
        table = [headers]
        
        for values in itertools.product([True, False], repeat=len(self.variables)):
            row = list(values)
            value_dict = dict(zip(self.variables, values))
            
            for expression in self.expressions:
                row.append(self.evaluate_expression(expression, value_dict))
            
            table.append(row)
        
        return table

    def display_truth_table(self):
        table = self.generate_truth_table()
        for row in table:
            print("\t".join(map(str, row)))

    def save_to_memory(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        memory_data = {
            "timestamp": timestamp,
            "variables": list(self.variables),
            "expressions": self.expressions
        }
        
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r+') as file:
                data = json.load(file)
                data.append(memory_data)
                file.seek(0)
                json.dump(data, file, indent=2)
        else:
            with open(self.memory_file, 'w') as file:
                json.dump([memory_data], file, indent=2)

    def load_from_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as file:
                data = json.load(file)
                if data:
                    latest_entry = data[-1]
                    self.variables = set(latest_entry["variables"])
                    self.expressions = latest_entry["expressions"]

def main():
    logic = LogicTables()
    logic.load_from_memory()
    logic.add_variable('P')
    logic.add_variable('Q')
    logic.add_expression('P and Q')
    logic.add_expression('P or Q')
    logic.add_expression('not P')
    logic.display_truth_table()

if __name__ == '__main__':
    main()

