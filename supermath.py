### Made by Mateo Ayala
### Alpha 2.2

import math
import sys
import os
from time import sleep
import numpy as np

print("Welcome to the Supermath Calculator v.2.2 :)")
print("\nNew interface! Now you can directly enter the operation in the input bar :D")
print("\nIn this version I restructured the code and defined several operations.")

def supermath():
    equation_solver = input("Do you wish to solve the pythagorean theorem, or do basic arithmetic? PT/BA: ")
    if equation_solver == "BA":
        basic_arithmetic()
    if equation_solver == "PT":
        pythagorean_theorem()
    if equation_solver != "BA" and equation_solver != "PT":
        print("Please enter a valid argument.")
    global final_confirmation
    final_confirmation = input("Would you like to start again? Y/N: ")

def basic_arithmetic():
    global number1
    number1 = input("Enter a number: ")
    global number2
    number2 = input("Enter another number: ")
    try:
        float(number1) + float(number2)
        global error_buster
        error_buster = True
    except ValueError:
        print("You have entered an invalid value. Please try again.")        
        error_buster = False
    if error_buster == True:
        confirmation = input("Please enter the equation you wish to solve."
         "\nYou can enter 'gcd' for greatest common denominator, 'addition', etc..: ")
        if confirmation == "addition":
            addition()
        elif confirmation == "subtraction":
            subtraction()
        elif confirmation == "multiplication":
            multiplication()
        elif confirmation == "division":
            division()
        elif confirmation == "gcd":
            gcd()
        elif confirmation == "lcm":
            lcm()
        elif confirmation == "power":
            power()
        elif confirmation == "root":
            root()
        else:
            print("Sorry, that's all I can do for now.")

def addition():
    result = float(number1) + float(number2)
    print(result)

def subtraction():
    result = float(number1) - float(number2)
    print(result)

def multiplication():
    result = float(number1) * float(number2)
    print(result)

def division():
    result = float(number1) / float(number2)
    print(result)

def gcd():
    result = math.gcd(int(number1), int(number2))
    print(result)

def lcm():
    result = math.lcm(int(number1), int(number2))
    print(result)

def power():
    result = float(number1)**float(number2)
    print(result)

def root():
    result = float(number1)**(1/float(number2))
    print(result)

def pythagorean_theorem():
    LT_confirmation = input("Are you trying to find lenght or width, or diagonal? LW/D: ")
    if LT_confirmation == "LW":
        lenght_width()
    if LT_confirmation == "D":
        diagonal()
    if LT_confirmation != "LW" and LT_confirmation != "D":
        print("Please enter a valid answer.")

def lenght_width():
    leg1 = input("Enter the lenght of the lenght or width: ")
    leg2 = input("Enter the lenght of the diagonal line: ")
    try:
        float(leg1) + float(leg1)
        error_buster = True
    except ValueError:
        print("You have entered an invalid value. Please try again.")
        error_buster = False
    if error_buster == True:
        leg_ans1 = float(leg1)**2
        leg_ans2 = float(leg2)**2
        leg_ans_final1 = leg_ans2 - leg_ans1
        leg_ans_final2 = math.sqrt(leg_ans_final1)
        print("The answer is:", leg_ans_final1, "before square root and", leg_ans_final2, "after square root.")

def diagonal():
    leg1 = input("Enter the lenght of the lenght: ")
    leg2 = input("Enter the lenght of the width: ")
    try:
        float(leg1) + float(leg2)
        error_buster = True
    except ValueError:
        print("You have entered an invalid value. Please try again.")
        error_buster = False
    if error_buster == True:
        leg_ans1 = float(leg1)**2
        leg_ans2 = float(leg2)**2
        leg_ans_final1 = leg_ans1 + leg_ans2
        leg_ans_final2 = math.sqrt(leg_ans_final1)
        print("The answer is:", leg_ans_final1, "before square root and", leg_ans_final2, "after square root.")
supermath()

while final_confirmation == "Y":
    os.system("cls")
    supermath()

if final_confirmation == "N":
    print("\nThank you for using this math tool :)")
    print("\nThis program will close in 5...")
    sleep(1)
    print("4...")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    sys.exit()