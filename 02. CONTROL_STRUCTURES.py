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
# (end_before_this_number)
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

"""==========================================================="""
# Nested FOR Loop

for x in range(5):
    print("A")
# will print 5 pero if number ang iprint mismo it will print 4 - 0,1,2,3,4

# example ng number ang print
for x in range(7):
    print(x)

for x in range(5):
    for y in range(5):
        print("*")
# meaning 5 times gagawin ung loop ng y therefore 25 times maeexecute

#To execute the loop in one line add end=""
#Kasi pagnagexecute ng loop laging new line after ng 1 execution
for x in range(5):
    for y in range(5):
        print("*", end="")

#printing the x
for x in range(6):
    for y in range(5):
        print("*", end="")
    print()
# Ung may print na may end is for y 
# Tas ung print na walang laman ay for x
# So ibig sabihin 5 na magkakadikit tas 6 na columns

"""
iprint niya muna ung y which is may 5 asterisk
then execute ung print() which is new line lang
then balik sa y hanggang matapos kung ano ung nakaindicate na range
"""