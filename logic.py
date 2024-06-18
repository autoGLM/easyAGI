# logic.py
import itertools

class LogicTables:
    def __init__(self):
        self.variables = set()
        self.expressions = []

    def add_variable(self, variable):
        self.variables.add(variable)

    def add_expression(self, expression):
        self.expressions.append(expression)

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

def main():
    logic = LogicTables()
    logic.add_variable('P')
    logic.add_variable('Q')
    logic.add_expression('P and Q')
    logic.add_expression('P or Q')
    logic.add_expression('not P')
    logic.display_truth_table()

if __name__ == '__main__':
    main()

