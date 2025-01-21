## Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable.
import math


def Variables(a,b,c):
    print("a=",a)
    print("Type of variable a is:",type(a))
    print("b=",b)
    print("Type of variable b is:",type(b))
    print("c=",c)
    print("Type of variable b is:",type(c))
Variables(1,1.0,'1')
##2.Redeclare the same variable as another number.(2,2.0 and ‘2’) and share your observation on result.
Variables(2,2.0,'2')

##. Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c..
a=b=c=10
print("a=",a)
print("b=",b)
print("c=",c)

## 4.Assign two variables a and b as integer and print the sum of a+b.
def Sum(a,b):
    c=a+b
    print("c=",c)
Sum(2,4)

##5.Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)

##6. How do you access the second and fourth elements from the list.
print("2nd element is:",fruits[1])
print("4th element is:",fruits[3])

##7.Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.
numbers = [10, 20, 30, 40, 50]
print("Before Modification numbers:",numbers)
numbers[2]=35
print("After Modification numbers:",numbers)

##Create a Tuple
##How do you create a tuple with the following elements: "red", "green", "blue"?
elements = ("red", "green", "blue")
print(elements)
print("type of element:",type(elements))

##How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?
colors = ("red", "green", "blue", "yellow")
print("First element and last element is respectively:", colors[0] + ",", colors[3])

##Immutable Nature of Tuples:What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?
colors[3]='black'
print(colors[3])
#TypeError: 'tuple' object does not support item assignment

##Tuple Unpacking:Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.
Tuple=(10, 20, 30)
x=Tuple[0]
y=Tuple[1]
z=Tuple[2]
print("x:", x)
print("y:", y)
print("z:", z)
print("x,y and z:",str(x) + ",",str(y) + ",",str(z))

##Check Element in Tuple:Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").
colors = ("red", "green", "blue")
for Check in colors:
    if Check == "blue":
        print("blue is present")
    else:
        print("blue is not present")

colors = ("red", "green", "blue")
for Check in colors:
    if Check == "blue":
        print("blue is present at index", colors.index(Check))

#Tuple Length:Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").
days=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("The length of the tuple is:",len(days))

##Create a Dictionary:Create a dictionary where the keys are student names and the values are their grades. For example:

Dict={"Alice": 85, "Bob": 90, "Charlie": 78}

#Access Dictionary Values:How do you access Bob's grade from the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}?

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
for stud,Age in students.items():
    print(f"{stud}: {Age}")
students_list = list(students.items())
print(students_list)
print(students_list[0])


##Add and Remove Key-Value Pairs:
# Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary.

students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print(students)
students["David"] = 92
del students["Charlie"]
print(students)

##Update Dictionary Values:
##Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["Bob"] = 95
print(students)

##Check if Key Exists in a Dictionary:
##Write a Python program to check if "Alice" is a key in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

if "Alice" in students:
    print("Alice is a key in the dictionary.")
else:
    print("Alice is not a key in the dictionary.")

##Dictionary Length:
# Write a Python program to find the number of key-value pairs in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("The number of key-value pairs in the dictionary is:",len(students))


# Operators in python - Exercise :
# Write a Program to find Maximum of 3 Numbers .
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if a>b and a>c:
    print("maximum value is:",a)
elif b>a and b>a:
    print("maximum value is:",b)
elif c>b and c>a:
    print("maximum value is:",c)


# Flow Control - Exercise :
# Write a Program to find Biggest of given 2 Numbers from the Key Board?
n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number"))
if n1>n2:
    print("Biggest Number is :",n1)
else:
    print("Biggest number is :",n2)

# 2. Write a Program to Check whether the given Number is in between 1 and 10?
n = int(input("Enter Number"))
if n>=1 and n<=10:
    print("The Number",n,"is in between 1 to 10" )
else:
     print("The Number",n,"is not between 1 to 10")

















