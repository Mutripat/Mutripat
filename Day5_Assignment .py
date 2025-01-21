##Assignment 1: Static Methods
##Create a class MathOperations that contains:
##A static method add_numbers that takes two arguments and returns their sum.
##A static method multiply_numbers that takes two arguments and returns their product.

class MathOperations:
    def sum(a,b):
        return(a+b)
    def product(a,b):
        return(a*b)
sum_of_no=MathOperations.sum(2,3)
pro_of_no=MathOperations.product(2,3)
print(f"sum of number:{sum_of_no}")
#print("sum of two number:",sum_of_no)
print(f"product of number:{pro_of_no}")
        
## Assignment 2: Class Methods
## Create a class Person that keeps track of the number of people created. The class should have:
## A class variable count to count instances of the class.
## A class method get_count that returns the current count.
class Person:
    count = 0
    def __init__(self, name):
       self.name = name
       Person.count += 1

    @classmethod
    def get_count(cls):
       return cls.count
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
print(f"Number of people created: {Person.get_count()}") 



class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def info(cls):
        return "This class contains methods for converting temperatures between Celsius and Fahrenheit."


temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)
info_message = TemperatureConverter.info()

print(f"25°C is {temp_in_fahrenheit}°F")  
print(info_message) 
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bark")

animal=Animal()
animal.sound()
dog=Dog()
dog.sound()

## Assignment 5: Multiple Inheritance
## Create two classes:
## Bird with a method fly that prints "Flying".
## Fish with a method swim that prints "Swimming".
## A class Duck that inherits from both Bird and Fish.
class Bird:
    def fly(self):
        print("Flying")
class Fish:
    def swim(self):
        print("Swimming")
class Duck(Bird,Fish):
    pass
duck = Duck()
duck.fly()
duck.swim() 

## Assignment 6: Abstract Class
## Use the abc module to create an abstract class Shape that contains:
## An abstract method area().
## Two concrete classes Circle and Rectangle that inherit from Shape and implement the area method.
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    
   
    @abstractmethod
    def area(self):
        pass

## Concrete class Circle inheriting from Shape
# class Circle(Shape):
    
#     def __init__(self, radius):
#         self.radius = radius
    
#    
#     def area(self):
#         return math.pi * self.radius ** 2

# ## Concrete class Rectangle inheriting from Shape
# class Rectangle(Shape):
    
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     
#     def area(self):        return self.width * self.height

# ## Example usage
# circle = Circle(5)
# rectangle = Rectangle(4, 6)

# print(f"Area of the circle: {circle.area()}")     
# print(f"Area of the rectangle: {rectangle.area()}") 

# class BankAccount:
#     def __init__(self):
#         self._balance = 0
#     def deposit(self, amount):

### Assignment 7: Encapsulation
### Create a class BankAccount that uses encapsulation:
### Private attributes _balance.
### Public methods deposit() and withdraw() that modify _balance safely.

class BankAccount:
    def __init__(self):
        self._balance = 0 
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}. New balance: ${self._balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """Withdraw money from the bank account."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self._balance}.")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Return the current balance."""
        return self._balance


account = BankAccount()
account.deposit(100)   
account.withdraw(50)     
account.withdraw(60)   
print(f"Current balance: ${account.get_balance()}") 

## Assignment 8: Polymorphism with Method Overriding
## Create two classes Cat and Dog with a method speak().
## The Dog class should implement speak() to print "Woof".
## The Cat class should implement speak() to print "Meow".

class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    def speak(self):
        print("Meow")
def animal_speak(animal):
    animal.speak() 
dog = Dog()
cat = Cat()
animal_speak(dog)
animal_speak(cat)

##Assignment 9: Polymorphism with Method Overloading
##Create a class Calculator with a method add() that:
##Can accept 2 or 3 arguments and returns their sum.
##Hint: Use default parameters to handle method overloading in Python.

class Calculator:
    def add(self, a, b, c=0):  # c has a default value of 0
        """Return the sum of two or three numbers."""
        return a + b + c
calc = Calculator()
sum_two = calc.add(5, 10)
print(f"Sum of two numbers (5 + 10): {sum_two}")  
sum_three = calc.add(5, 10, 15)
print(f"Sum of three numbers (5 + 10 + 15): {sum_three}")  

##Assignment 10: Multilevel Inheritance
## Create three classes:
## LivingBeing with a method breathe() that prints "Breathing".
## Mammal that inherits from LivingBeing and adds a method walk() that prints "Walking".
## Human that inherits from Mammal and adds a method think() that prints "Thinking".

# Base class
class LivingBeing:
    def breathe(self):
        """Method to simulate breathing."""
        print("Breathing")

# Derived class Mammal
class Mammal(LivingBeing):
    def walk(self):
        """Method to simulate walking."""
        print("Walking")


class Human(Mammal):
    def think(self):
        """Method to simulate thinking."""
        print("Thinking")


if __name__ == '__main__':
    
    human = Human()
    
    
    human.breathe()  # Output: Breathing
    human.walk()     # Output: Walking
    human.think()    # Output: Thinking

