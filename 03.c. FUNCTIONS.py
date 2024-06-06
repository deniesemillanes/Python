# [Section] Functions
# Functions are block of code that runs when called.
# A function can be used to get inputs, process inputs and return inputs
# The "def" keyword is used to create a function. The syntax:
#  def <function_name>()

# defines a function called my_greeting
def my_greeting():
	print("Hello user!")

# Calling or Invoking a function - To use a function, just specify the function name and provide the value/values needed if there are.
my_greeting()

# Parameters can be added to functions to have more control to what the inputs for the function will be.

def greet_user(username):
	print(f'Hello, {username}')



# Arguments are the vlues that are submitted to the parameters
greet_user("Milk")

# Return statements - the "return" keyword allow functions to return values

def addition(num1, num2):
	return num1 + num2

sum = addition(5, 9)
print(f'The sum is {sum}!')
print(addition(5,9))

# [Section] Lambda Functions
# A lambda function is a small anonymous function that can be used for callbacks
# It is just like any normal python function, except that it has no name when defining it, and it is contained in one of code

# A lambda funciton can take any number of arguments but can only have one expression

greeting = lambda person: f'hello {person}'

greet = greeting("Elsie")
print(greet)

mult = lambda a, b : a * b

print(mult(5, 6))
