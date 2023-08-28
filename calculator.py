from operations import Addition, Subtraction, Multiplication, Division

class Calculator:
    def calculate(self, operation, a, b):
        if operation == "+":
            return Addition.perform(a, b)
        elif operation == "-":
            return Subtraction.perform(a, b)
        elif operation == "*":
            return Multiplication.perform(a, b)
        elif operation == "/":
            return Division.perform(a, b)
        else:
            raise ValueError("Unsupported operation")

    def supported_operations(self):
        return ["+", "-", "*", "/"]