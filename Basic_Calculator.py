import math

class Calculator:
    def __init__(self):
        self.history = [] #the list of calculation history

    def add(self, first_num, second_num):
        result = first_num + second_num
        self.history.append(f"{first_num} + {second_num} = {result}")
        return result

    def substract(self, first_num, second_num):
        result = first_num - second_num
        self.history.append(f"{first_num} - {second_num} = {result}")
        return result

    def multiply(self, first_num, second_num):
        result = first_num * second_num
        self.history.append(f"{first_num} * {second_num} = {result}")
        return result

    def divide(self, first_num, second_num):
        if second_num == 0:
            return "ERROR! You can not divide by Zero!"
        result = first_num / second_num
        self.history.append(f"{first_num} / {second_num} = {result}")
        return result
    
    def power(self, first_num, second_num):
        result = first_num ** second_num
        self.history.append(f"{first_num} ^ {second_num} = {result}")
        return result
    
    def sqaure_root(self, first_num):
        if first_num < 0:
            return "ERROR! Square root of a negative number!"
        result = math.sqrt(first_num)
        self.history.append(f"√{first_num} = {result}")
        return result
    
    def sin(self, first_num):
        result = math.sin(math.radians(first_num)) #Converting degrees to radians
        self.history.append(f"sin({first_num}°) = {result}")
        return result
    
    def cos(self, first_num):
        result = math.cos(math.radians(first_num)) #Converting degrees to radians
        self.history.append(f"sin({first_num}°) = {result}")
        return result
    
    def show_history(self):
        if not self.history:
            return "The History is empty."
        return "\n".join(self.history)

def basic_calculator():
    print("Please enter two numbers")
    try:
        first_num = float(input("First num:"))
        second_num = float(input("Second num:"))
    except ValueError:
        return "ERROR! Please enter numeric values"

    operation = input("Please choose operation(+, -, *, /): ")

    if operation == '+':
        result = add(first_num, second_num)
    elif operation == '-':
        result = substract(first_num, second_num)
    elif operation == '*':
        result = multiply(first_num, second_num)
    elif operation == '/':
        result = divide(first_num, second_num)
    else:
        result = "ERROR! Wrong operation!"

    return f"Answer: {result}"

#Start the Calculator
print (basic_calculator())

