# [Section] Classes
# Classes would serve as blueprints to describe the concept of objects
# Each Object has characteristics (properties) and behaviors (method)

# To create a Class, the "class" keyword is used along with the class name that starts with an uppercase character

class Car():
	# properties that all car Car objects must have are defined in a method called init

	# initializing the properties of our function
	def __init__(self, brand, model, year_of_make):
		self.brand = brand
		self.model = model
		self.year_of_make = year_of_make

		# propeties that are hard coded
		self.fuel = "Gasoline"
		self.fuel_level = 0

	# method
	def fill_fuel(self):
		print(f'Current fuel level: {self.fuel_level}.')
		print('filing up the fuel tank . . .')
		self.fuel_level = 100
		print(f'New fuel level: {self.fuel_level}.')


	def drive(self, distance):
		print(f'The car has driven {distance} kilometers!')

		self.fuel_level = self.fuel_level - distance

		print(f'The fuel left: {self.fuel_level}')




# intantiate a class
new_car = Car("Nissan", "GT-R", 2019)

print(new_car.brand)
print(new_car.model)
print(new_car.year_of_make)

print(new_car)
# to invoke a method
new_car.fill_fuel()
print(new_car.fuel_level)

new_car.drive(50)
print(new_car.fuel_level)
