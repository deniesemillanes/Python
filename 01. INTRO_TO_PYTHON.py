# Command to run programs in python
"""
on Windows:
    python <filename.py>

on Mac:
    python3 <filename.py>
"""

# Python Syntax
print("Hello")

# Indentation
"""
-- Used to indicate a block of code
"""

# Variables
"""
-- Are the container of data
"""

# Python Identifier
"""
-- Is the name we give to identify a variable, function, class, module or other object
-- Should begin with a letter (A to Z or a to z), dollar sign ($), or an underscore(_)
-- Uses Snake Case Convention
-- Are case sensitive
-- Allows assigning of values to multiple variables in one line
"""

age = 25
middle_initial = "C"
name1, name2, name3 = "Milk", "Pansa", "Angela Giarratana"

print(name2)

# Data Types
"""
Commonly used:

Text Type:	str
Numeric Types:	int, float, complex
Boolean Type:	bool
"""

password = "ink@12$"    #str
number = 22             #int
pi = 3.14               #float
complex = 1+5j          #complex
isLearning = True       #bool

# Using variables
print("Hi " + name1)
print(name1 + " " + name2)

# print() Function
# Concatenation
"""
-- we can use plus(+) sign or f string
"""
print(f"Hi {name1} this is a sample of f string")

# print("My age is " + age)       #THIS WILL HAVE AN ERROR - TypeError: can only concatenate str (not "int") to str

# Typecasting
"""
-- is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users
"""
""" To convert value into a string"""
print("My age is " + str(age))
"""
int() - to convert into integer
float() - to convert into float
"""
print(int(3.75))        #3
print(float(5))         #5.00

# Operators
"""
-- Are used to perform operations on variables and values
"""

# Arithmetic Operators
"""
-- Addition(+)
-- Subtraction(-)
-- Multiplication(*)
-- Division(/)
-- Modulus(%)   - kung ano ung remainder
-- Exponentiation(**)
"""

# Assignment Operators
"""
-- equal sign(=)
-- += , -= , *= , /= , %=
"""
num1 = 7
num1 +=3    #(num1 = num1+3)
print(num1) #10

# Comparison Operators
"""
==
!=
>=
<=
>
<
"""

print(1 == "1")     #False dahil ung isa ay string

# Logical Operators
"""
-- Used to combine conditional statements
-- or, and, not
"""

print(True or False)        #True
print(True and False)       #False
print(not False)            #True

