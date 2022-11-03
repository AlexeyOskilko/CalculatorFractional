class Calculator:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def substract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2

    def desicion(self, user_desicion):
        if user_desicion == '+':
            return self.add()
        elif user_desicion == "-":
            return self.substract()
        elif user_desicion == "*":
            return self.multiply()
        elif user_desicion == '/':
            return self.divide()