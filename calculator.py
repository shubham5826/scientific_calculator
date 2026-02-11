from basic_operations import *
from advanced_operations import *

def evaluate_expression():
    print("Scientific Calculator")
    print("1.Add 2.Subtract 3.Multiply 4.Divide")
    print("5.Sqrt 6.Power 7.Sin")

    choice = int(input("Enter choice: "))

    if choice in [1,2,3,4,6]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

    elif choice in [5,7]:
        a = float(input("Enter number: "))

    if choice == 1:
        print(add(a,b))
    elif choice == 2:
        print(subtract(a,b))
    elif choice == 3:
        print(multiply(a,b))
    elif choice == 4:
        print(divide(a,b))
    elif choice == 5:
        print(square_root(a))
    elif choice == 6:
        print(power(a,b))
    elif choice == 7:
        print(sin(a))
