from calculator import Calculator

def main():
    calculator = Calculator()

    print("Supported operations:", calculator.supported_operations())
    operation = input("Enter operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    try:
        result = calculator.calculate(operation, num1, num2)
        print("Result:", result)
    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()