# 1.Write a Python function to find the maximum of three numbers
def max(a,b,c):
    if a>b and b>c:
        print("Maximum number is :",a)
    elif b>a and a>c:
        print("Maximum number is :",b)
    else:
        print("Maximum number is :",c)
max(3,7,10)

# 2.Write a Python function to multiply all the numbers in a list.Sample List : (8, 2, 3, -1, 7)
def multi(a,b,c,d,e):
    multi=a*b*c*d*e
    print("Multiplication of these numbers is :",multi)
multi(8,2,3,-1,7)

# 3.Write a Python program to reverse a string.
def reverse(string):
    reverse_string=string[::-1]
    print("reverse string is :",reverse_string)
reverse("1234abcd")

#.4. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.
def factorial(n):
    if n== 1:
        return 1
    elif n>1:
        return n * factorial(n - 1)

number = 5
print(f"The factorial of {number} is: {factorial(number)}")

# 5. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def distinct_elements(input_list):
    return list(set(input_list))


original_list = [1, 2, 3, 2, 1, 4, 5, 3]
distinct_list = distinct_elements(original_list)
print(f"Original List: {original_list}")
print(f"Distinct List: {distinct_list}")

# 6.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
    return True 

number = 6
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# 7.Write a Python program to print the even numbers from a given list.
def even(n):
    if n % 2==0:
        print(f"{n} is Even number")
    else:
        print(f"{n} is not Even number")
number =8
even(number)

# 8.Write a Python function that accepts a string and counts the number of upper and lower case letters.
def count_case_letters(input_string):
    upper_count = 0
    lower_count = 0
    
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    return upper_count, lower_count


input_str = "The quick Brow Fox"
upper, lower = count_case_letters(input_str)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

# 9.Write a Python function to sum all the numbers in a list.

def sum_numbers(num_list):
    total = sum(num_list) 
    return total
numbers = [8,2,3,0,7]
result = sum_numbers(numbers)
print(f"The sum of the numbers in the list is: {result}")

# 10. Write a  Python function that checks whether a passed string is a palindrome or not.
def is_palindrome(input_string):
    
    cleaned_string = ''.join(input_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]
test_string = "A man a plan a canal Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')





    










