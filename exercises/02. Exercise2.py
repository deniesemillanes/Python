#1 Create and if-else statement that determines if a number is divisible by 3, 5 or both
#2 Leap year:
"""
-- Accept a year input from the user and determine if it is a leap year or not.
-- Accept two numbers (row and col) from the user and create a grid of asterisks using the two numbers (row and col).
-- Add a validation for the leap year input:
    - Strings are not allowed for inputs
    - No zero or negative values
"""

# 1

# num = int(input("Num:"))

# if num%3 ==0 and num%5 == 0:
#     print("Divisible by 3 and 5")
# elif num%3 ==0:
#     print("By 3")
# elif num%5 ==0:
#     print("By 5")
# else:
#     print("Not divisible by 3 nor 5")

#2
# year = int(input("Year:"))

# if year%4==0 and year>0:
#     print("Leap year")
# elif type(year)==str:
#     print("Don't input string")
# else:
#     print("Not leap year")

"""
============================================
year = input("Year:")

if type(year)==str:
    print("This is a string")
elif type(year)==int:
    if year%4==0 and year>0:
        print("Leap year")
    elif year<0:
        print("Input positive number")
    else:
        print("Not leap year")
else:
    print("Input a number")
============================================
"""  

#3
row = int(input("Row:"))
col = int(input("Col:"))

for x in range(0, row):
    for y in range(0, col):
        print("*", end=" ")
    print()

"""========================================="""
# Pattern
'''-- nested for loop'''

for x in range(5):
    print("A")
# will print 5 pero if number ang iprint mismo it will print 4 - 0,1,2,3,4

# Continue sa 02.CONTROL_STRUCTURES.py for discussion