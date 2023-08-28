
class Addition:
    @staticmethod
    def perform(a, b):
        return a + b

class Subtraction:
    @staticmethod
    def perform(a, b):
        return a - b

class Multiplication:
    @staticmethod
    def perform(a, b):
        return a * b

class Division:
    @staticmethod
    def perform(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is not allowed")