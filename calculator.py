class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("Calculator module demo")
    print("----------------------")
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 7 = {calc.subtract(5, 7)}")
    print(f"4 * 6 = {calc.multiply(4, 6)}")
    print(f"8 / 2 = {calc.divide(8, 2)}")
