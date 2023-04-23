
# Variables
x = 5
y = "Hello, World!" # Strings are surrounded by either single or double quotation marks
print(x)
print(y)
print(y)

# Data types
print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'str'>

# Loops
for i in range(5):
    print(i)

# Conditional statements
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Functions
def square(x):
    return x**2

print(square(4)) # Output: 16

# Modules
import math
print(math.pi) # Output: 3.141592653589793

class Dog:
    # Class attribute
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def saySpecies():
        print("My species is " + Dog.species)

    def sayName(self):
        print("My name is " + self.name)

# Instantiate the Dog object
a = Dog("Max", 5)
print(type(Dog))
print(type(a))

# Access the instance attributes
print(a.name)

# Creating more instances
b = Dog("Maxib", 5)
c = Dog("Maxc", 5)

def sayNameFn(lst):
    print("My name is " + lst[0])

dogs = [["Max", 5], ["Max", 5], ["Max", 5]]
for dog in dogs:
    print('feature 01')
    print('feature 02')
    sayNameFn(dog) # Output: My name is dog.name

a.sayName() # a is an instance of the Dog class
Dog.saySpecies() # Dog is the class itself
Dog.sayName()