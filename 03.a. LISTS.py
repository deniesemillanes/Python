# 4 built-in data types in Python
'''
    1. LIST
        is a collection which is ordered and changeable. Allows duplicate members.
    2. TUPLE
        is a collection which is ordered and unchangeable. Allows duplicate members.
    3. SET
        is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    4. DICTIONARY
        is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''
# List
"""
-- Lists are used to store multiple items in a single variable.
-- created using square brackets
"""

names = ["Milk", "Pansa", "Vosbein"]  #String List
programs = ["developer career", "pi-shape", "short courses"] #string list
durations = [260, 180, 20] #Number List
truth_variables = [True, False, True, True, False] #Boolean List

sample_list = ["Apple", 3, False, "Potato", 4, False]   # A List can contain elements with different data types:

# type() function  
"""
prints what type of data structures are used
"""
print(type(names))      #output: <class 'list'>

# list()
"""
is a Python built-in function that generates a list from an iterable provided as an argument.
"""
flowers = list(('Sunflower', 'Daisy', 'Tulip', 'Lavender', 'Rose'))
print(flowers)  #output: ['Sunflower', 'Daisy', 'Tulip', 'Lavender', 'Rose']

# len() method
"""
-- counts the number of elements in a list
"""
print(len(sample_list))

var_len=len(names)
print(var_len)

# Accessing values/elements in a list
"""
-- can be accessed by providing the index number of the element
"""
print(names[0])     #Milk
print(names[-1])    #sa dulo ng list - Vosbein
print(programs)     #prints the whole list
print(truth_variables[0:2])    #prints a range of values

# Updating Lists
print(f"Current value: {programs[2]}")

programs[2] = "ShortCourses"    # Update the value
print(f"New value: {programs[2]}")

# LIST MANIPULATION

# append()
"""
-- adds an element at the end of the list.
"""
programs.append("global")
print(programs)     #output: ['developer career', 'pi-shape', 'ShortCourses', 'global']

# del
"""
-- if you do not specify the index, the pop() method removes the last item
-- can also delete the list completely
"""
print (durations)   #[260, 180, 20]
del durations[-1]
print (durations)   #[260, 180]

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist) #['apple', 'cherry']

del thislist

# insert
"""
-- Inserts an element into the list at the specified location.
-- It takes two arguments: the index where the element is inserted and the element itself.
-- Insert another item (index_place, value)
"""
programs.insert(2, "python")
print(programs) #output: ['developer career', 'pi-shape', 'python', 'ShortCourses', 'global']

# "in" keyword
"""
-- Membership checking - the "in" keyword checks if the element is in the list
"""
print(260 in durations) #output: True
print(500 in durations) #output: False

# sort() method 
"""
-- sorts the list alphanumerically, ascending, by default.
"""
durations.sort()
print(durations)    #output: [180, 260]
durations.sort(reverse = True)  #To sort descending, use the keyword argument reverse = True:
print(durations)    #output: [260, 180]

# clear() method
"""
-- is used to empty the contents of the list
-- The list still remains, but it has no content.
"""
test_list = [1, 3, 5, 7, 9]
print(test_list)

test_list.clear()
print(test_list)    #output: []