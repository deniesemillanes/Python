# One Function Calculator
"""
    Try to create a program that will perform the arithmetic operators when the user inputs 2 numbers
"""

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("One Function Calculator")
add = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2

print(f"For additon: {num1}+{num2} = {add}\n")
print(f"For subtraction:{num1}-{num2} = {sub}\n")
print(f"For multiplication:{num1}*{num2} = {mult}\n")
print(f"For division: {num1}/{num2} = {div}\n")