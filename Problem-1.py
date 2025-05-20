class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero is not allowed."
        else:
            return "Invalid operation"


calc = Calculator(10, 5)
print("Add:", calc.operate("add"))
print("Subtract:", calc.operate("subtract"))
print("Multiply:", calc.operate("multiply"))
print("Divide:", calc.operate("divide"))
