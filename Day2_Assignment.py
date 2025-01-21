#Assignment:
#Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
def Calculation(n1 = int(input("Enter First Number is : ")),n2 = int(input("Enter Second Number is :"))):
    print("Addition of n1 & n2:",(n1 + n2))
    print("Substraction of n1 & n2:",(n1 - n2))
    print("Multiplication of n1 & n2:",(n1*n2))
    print("Divison of n1 & n2 :",(n1/n2))
    print("Modulus of n1 & n2 :",(n1%n2))
Calculation()

#Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.
def oddeven(n):
    if n % 2 ==0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")
oddeven(15)

#Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.
n= int(input("Enter Number :"))
if n >0:
    print(f"{n} is positive number")
elif n ==0:
    print("n is zero")
else:
    print(f"{n} is negative number")


#Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:
n = int(input("Student number :"))
if n >=90:
    print(f"Student got {n}% and grade is A")
elif n>=80 and n<90:
    print(f"Student got {n}% and grade is B")
elif n>=70 and n<80:
    print(f"Student got {n}% and grade is C")
elif n>=60 and n<70:
    print(f"Student got {n}% and grade is D")
else:
    print(f"Student got {n}% and grade is F")

# Question 5: Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.

with open('sample.txt', 'w') as file:
    file.write("Hello, this is a sample file.")

with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

# Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.

def count_words_simple(filename):
    word_count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                word_count += len(line.split())
        return word_count
    except FileNotFoundError:
        return "File not found."


filename = 'data.txt'
print("Number of words:", count_words_simple(filename))


#Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.

x =1
while x <=10:
    print(x)
    x=x+1

#Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.

n = int(input("Enter any number :"))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")















