def add(first_num, second_num):
    return first_num + second_num

def substract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    if second_num == 0:
        return "ERROR! You can not divide on Zero!"
    return first_num / second_num

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

