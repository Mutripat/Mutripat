# #1. Write a Python program to create a class named Car. Define attributes like brand, model, and year. 
# #   Create an object of the class and display the details of the car?

# class Car:
#     brand="Hyundai"
#     model="i-20"
#     year="2022"
# s1=Car
# print(s1.brand,s1.model,s1.year)

# #2. Create a class Student with attributes name, roll_number, and marks. 
# # Define a constructor to initialize these attributes and a method display_info() to print the student's details?

# class Student:
#     def __init__(self, name, roll_number, year):
#         self.name=name
#         self.roll_number=roll_number
#         self.year=year
#         print("adding new student name")
# s1 = Student("Ashish", "i-20", "2022")
# s2 = Student("John", "i-21", "2023")
# print(s1.name,s2.name)
# print(s1.roll_number,s2.roll_number)
# print(s1.year,s2.year)

# #3. Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. 
# # Create multiple objects and display the area and perimeter for each?

# class Rectangle:
#     def __init__(self,Length,width):
#         self.Length=int(Length)
#         self.width=int(width)
# s1=Rectangle("20","10")
# Area=(s1.Length)*(s1.width)
# Perimeter=2*(s1.Length+s1.width)
# print("Area:",Area,"Perimeter:",Perimeter)

# #4. Write a class Circle with an attribute radius and methods get_area() and get_circumference(). 
# # These methods should return the area and circumference of the circle, respectively ?

# class Circle:
#     def __init__(self,radius):
#         self.radius=int(radius)
#     def get_area(self):
#         return 3.14*(self.radius**2)
#     def get_circumference(self): 
#         return 2*3.14*self.radius
# s1=Circle("10")
# print(f"Area: {s1.get_area():.2f}")
# print(f"Circumference: {s1.get_circumference():.2f}")

# #5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

# class Account:
#     def __init__(self,account_no, balance):
#         self.account_no = account_no
#         self.balance = balance
#     def debit(self,amount):
#         if amount>self.balance:
#             print(f"Insufficient balance. Available balance is {self.balance:.2f}")
#         else:
#              self.balance =self.balance- amount
#     def credit(self,amount):
#         self.balance =self.balance+ amount
#     def print_balance(self):
#         print(f"Account No: {self.account_no}, Balance: {self.balance:.2f}")
        
# acc = Account("123456789", 1000)
# acc.print_balance()
# acc.debit(500)
# acc.print_balance()
# acc.credit(1500)
# acc.print_balance()

# #6. Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the 
# # count whenever a new employee object is created.Show the updated employee count after creating new objects.

# class Employee:
#     def __init__(self,employee_count):
#         self.employee_count = employee_count
#     def increment_employee_count(self,New_employee_Count):
#         self.employee_count =self.employee_count+ New_employee_Count
#         print(f"Updated Emplyoee:{self.employee_count}")
# s1=Employee(10000)
# s1.increment_employee_count(500)

# ## 7.Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes 
# ## or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method.

# class Book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price
#     def details(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: ${self.price:.2f}")
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 15.99)
# book1.details()
# # 8.Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns 
# # its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.

# class TemperatureConverter:
#     def __init__(self,celsius):
#         self.celsius = celsius
#     def celsius_to_fahrenheit(self):
#         fahrenheit = self.celsius *(9/5) + 32
#         return (self.celsius *(9/5) + 32)
#         #print(f"fahrenheit:{fahrenheit}")
# s1=TemperatureConverter(37)
# print(f"fahrenheit:{s1.celsius_to_fahrenheit()}")

# #9. Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object, 
# # adds its values to the current object, and returns a new Time object with the resulting sum.

# class Time:
#     def __init__(self,hours,minutes):
#         self.hours = hours
#         self.minutes = minutes
#     def add_time(self,new_hours,new_minutes):
#         current_minutes=self.minutes+new_minutes
#         current_hours=self.hours+new_hours
#         if current_minutes>=60:
#             current_hours=current_hours+(current_minutes//60)
#             current_minutes=current_minutes % 60
#         print("current_hours:current_minutes",current_hours,current_minutes)
# s1=Time(5,40)
# s1.add_time(4,50)

#10.Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method set_bonus_percentage() to change 
# the bonus percentage for all employees.Create an instance method calculate_total_salary() to calculate and 
# return the total salary (basic + bonus) for a specific employee

class EmployeeSalary:
    def __init__(self,basic_salary):
        self.basic_salary = basic_salary
        # self.bonus_percentage = bonus_percentage
    @classmethod
    def set_bonus_percentage(cls,bonus_percentage):
        cls.bonus_percentage = bonus_percentage
    def calculate_total_salary(self):
        total_salary=self.basic_salary+(self.basic_salary*(EmployeeSalary.bonus_percentage/100))
        print("total_salary:",total_salary)
s1=EmployeeSalary(10000)
s1.set_bonus_percentage(20)
s1.calculate_total_salary()

# class EmployeeSalary:
#     def __init__(self,basic_salary,bonus_percentage):
#         self.basic_salary = basic_salary
#         self.bonus_percentage = bonus_percentage
# s1=EmployeeSalary(10000,20)
# total_salary=s1.basic_salary+s1.basic_salary*(s1.bonus_percentage/100)
# print("total_salary:",total_salary)




        




        





