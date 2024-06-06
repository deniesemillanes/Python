# DICTIONARIES
"""
    are used to store data values in key:value pairs
    A dictionary is a collection which is ordered, changeable and does not allow duplicates
    To create a dictionary, the curly braces ({}) is used and the key:value pairs are denoted with (key: value)
"""

person1 ={
	"name" : "Milk",
	"age": 27,
	"occupation" : "student",
	"isEnrolled" : True,
	"subjects" : ["Python", "SQL", "Django"]
}

# len() method
# To get the number of key-value pairs on the dictionary
print(len(person1))

# The keys() method
# will return a list of all the keys in the dictionary
print(person1.keys())

# the values() method
# will return a list of all the values in the dictionary
print(person1.values())

# The items() method
# will return each item in a dictionary as key-value pair in a list
print(person1.items())

# Accessing values in dictionary
# To get item in the dictionary, the key name can be referred using square bracket([])
print(person1["name"])
# print(person1.name)

# Adding key-value pairs can be done with either a new index key and assigning a value or the update method
# index key
person1["nationality"] = "Filipino"
print(person1)

# update method
person1.update({"fav_food": "Sinigang"})
print(person1)

# pop method
# removes the item with the specified key name
person1.pop("name")
print(person1)

# using the del keyword
# removes the item with the specified key name
del person1["nationality"]
print(person1)

# The clear() method empties the dictionary
person2 = {
	"name" : "John",
	"age" :18
}
# person2.clear()



# LOOPING THROUGH DICTIONARY

"""Print all key names in the dictionary, one by one"""
for x in person2:
  print(x)
	# OUTPUT:
	# name
	# age
print("\n or using keys() ")
for x in person2.keys():
	print(x)

"""Print all values in the dictionary, one by one"""
for x in person2:
  print(person2[x])
	# OUTPUT:
	# John
	# 18
print("\n or using values() ")
for x in person2.values():
  print(x)

print("\n")

"""Loop through both keys and values, by using the items() method"""
for x, y in person2.items():
  print(f"key is {x} and value is {y}")

# Nested dictionaries - dictionaries can be nested inside each other
"""A dictionary can contain dictionaries, this is called nested dictionaries."""

print("\n")
print("Nested dictionaries")

person3 = {
	"name": "Monika",
	"age" : 20,
	"occupation": "poet",
	"isEnrolled": True,
	"subjects" : ["Python", "SQL", "Django"]
}


print(person3["subjects"][0])
#printing the value of the person3>subjects>order -1
print(person3["subjects"][-1])

student1 = "student1"
student2 = "student2"

# created a dictionary containing the other two dictionaries which is person1 and person3:

class_room = {
	student1 : person1,
	student2 : person3
}

#printing the value of the student2>subject>order 1
print(class_room["student2"]["subjects"][1])
