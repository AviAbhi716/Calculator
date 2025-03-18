import os
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
operation_dict = {
         '+':add,
         '-':sub,
         '*':mul,
         '/':div
    }
def calculate():
    num1 = int(input("Enter first number:"))
    for i in operation_dict:
        print(i)
    game = True
    while game:
        operation = input("Pick an operation:")
        num2 = int(input("Enter second number:"))
        calculation_function = operation_dict[operation]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        check = input(f"Enter 'y' to continue calculation with {result} or 'n' to start new calculation or 'x' to exit").lower()
        if check == 'y':
            num1 = result
        elif check == 'n':
            game = False
            os.system('cls')
            calculate()
        else:
            game = False
            print("Thank You")
calculate()
