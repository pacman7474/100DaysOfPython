# def calculate(num1,num2,operator):
#     match operator:
#         case "+":
#             return num1 + num2
#         case "-":
#             return num1 - num2
#         case "*":
#             return num1 * num2
#         case "/":
#             return num1 / num2
#
# print("Welcome to the calculator")
# first_num = int(input("What is your first number?> "))
# operation = input("What operation are you using?\n+\n-\n*\n/\n")
# second_num = int(input("What is your second number?> "))
# print(f"{first_num} {operation} {second_num} = {calculate(first_num,second_num,operation)}")

def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def multiply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
repeat = True
print("Welcome to the calculator")
first_num = int(input("What is your first number?> "))
while repeat:
    for op in operations:
        print(op)
    operation = input("What operation are you using?> ")
    second_num = int(input("What is your second number?> "))
    total_num = operations[operation](first_num,second_num)
    print(f"{first_num} {operation} {second_num} = {total_num}")
    cont = input("Do you want to continue? (y/n)> ").lower()
    if cont == "y":
        repeat = True
        first_num = total_num
        print(f"Your first number is {first_num}")
    else:
        repeat = False
        print("Thank you for using the calculator. GoodBye.")