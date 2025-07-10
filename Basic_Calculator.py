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
        self.history.append(f"Root of {first_num} = {result}")
        return result
    
    def sin(self, first_num):
        result = math.sin(math.radians(first_num)) #Converting degrees to radians
        self.history.append(f"sin({first_num}°) = {result}")
        return result
    
    def cos(self, first_num):
        result = math.cos(math.radians(first_num)) #Converting degrees to radians
        self.history.append(f"cos({first_num}°) = {result}")
        return result
    
    def show_history(self):
        if not self.history:
            return "The History is empty."
        return "\n".join(self.history)



#Testing class
calc = Calculator()
print(calc.add(28, 40)) #68
print(calc.substract(2035, 2030)) #5
print(calc.multiply(20, 4)) #80
print(calc.divide(20, 4)) #5.0
print(calc.divide(20, 0)) #Zero check
print(calc.power(2, 10)) #1024
print(calc.sqaure_root(21)) #4.58257569495584
print(calc.sin(21)) #0.35836794954530027
print(calc.cos(52)) #0.6g the156614753256583

print(calc.show_history())
