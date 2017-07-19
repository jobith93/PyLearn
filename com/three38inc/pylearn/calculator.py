#!/usr/bin/python3
# simple text mode int calculator using python
# global variables
num1 = 0
num2 = 0
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]


def print_menu():
    """"function to print menu and get choice"""
    print("Simple Calculator\n=================")
    print("1. Addition")
    print("2. subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    return int(input("Enter your choice: "))


def get_input():
    """function to get input for 2 numbers"""
    global num1, num2
    num1 = int(input("Enter value for number 1: "))
    num2 = int(input("Enter value for number 2: "))
    return


def calculate(ch=0, n1=0, n2=0):
    """function for calculations"""
    if ch == 1:
        return n1 + n2
    elif ch == 2:
        return n1 - n2
    elif ch == 3:
        return n1 * n2
    elif ch == 4:
        return n1 / n2
    elif ch == 5:
        return n1 ** n2
    else:
        return 0


def main():
    """main driver program"""
    choice = print_menu()
    get_input()
    if 0 < choice < 6:
        print("Answer after", operations[choice - 1], "is :", calculate(choice, num1, num2))
    else:
        print("Invalid Choice")

    redo = input("Would you like to run again ? (y/n) ")

    if redo == 'y' or redo == 'Y':
        main()
    else:
        print("Thank you! Keep Coding...")


# main program
main()
