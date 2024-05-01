"""
=========================================================================================
# User input
username = input("Please enter your username: \n")
print(f"Welcome {username}")

num1 = input("Enter first number:")
num2 = input("Enter second number:")
# This will concatinate the number and won't add 
print(f"Sum of 2 numbers: {num1+num2}")
# typecast the input number
num3 = int(input("Enter third number:"))
num4 = int(input("Enter fourth number:"))
print(f"Sum of 2 numbers: {num3+num4}")
=========================================================================================
"""


"""
=========================================================================================
# Control Structures

'''
-- divided into selection and repitition control structures
-- selection control structures - have conditions
-- repetition control structures - repeat certain blocks of code
'''


# If-else statement
test_num = 75

if test_num >=60 :
    print("Test passed")
else:
    print("Test failed")

# If-elif-else statement

test_num2 = int(input("Second number:"))

if test_num2 >0:
    print("The number is positive")
elif test_num2 ==0:
    print("The number is equal to 0")
else:
    print("The number is negative")
=========================================================================================
"""


# Loops
"""
-- are used to execute a set of statements as long as the condition is true
"""

i =0

while i <=5:
    print(f"Current value of i is {i}")
    i +=1 
    # i = i+1

# Iteration over a sequence

fruits = ["apple", "banana", "cherry"]      #lists

for indiv_fruit in fruits:
    print(indiv_fruit)

# range() method
'''
use the for loop to iterate through values, the range method can be used
'''

# default starting value is 0
# (stops_at_this_number)
for x in range(6) :
    print(f"The current value of x is {x}")

# (start, end_before)
for x in range(6, 10) :
    print(f"The current value of x is {x}!")

# (start, end_before, increment)
for x in range(6, 20, 2) :
    print(f"The current value of x is {x}~")

"""
=========================================================================================
# Break Statement
'''
-- The break statement is used to stop the loop
'''

j=1
while j<6 :
    print(j)

    if j==3 :
        break
    j+=1
=========================================================================================
"""

# [Section] Continue Statement
# The continue statement returns the control to the beginning of the while loop and continue to the next iteration

k=1
while k<6 :
    k+=1
    
    if k==3 : 
        continue
    
    print(k)