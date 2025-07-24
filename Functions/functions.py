'''
Q1) Write a function to return the sum of all numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''

def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
sample_list = (8, 2, 3, 0, 7)
print(sum_of_list(sample_list))

'''
Q2) Write a function to return the reverse of a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''
def reverse_string(s):
    return s[::-1]
sample_string = "1234abcd"
print(reverse_string(sample_string))

'''
Q3) Write a function to calculate and return the factorial of a number (a non-negative integer).
'''
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(5))

'''
Q4) Write a function that accepts a string and prints the number of upper case letters and lower case
letters in it.
'''

def count_case(s):
    upper_case_count = 0
    lower_case_count = 0
    for char in s:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
    return upper_case_count, lower_case_count
sample_string = "Hello World"
upper_count, lower_count = count_case(sample_string)
print(f"Upper case letters: {upper_count}, Lower case letters: {lower_count}")

'''
Q5) Write a function to print the even numbers from a given list. List is passed to the function as an
argument.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''
def print_even_numbers(numbers):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(print_even_numbers(sample_list))

'''
Q6) Write a function that takes a number as a parameter and checks whether the number is prime or not.
'''
import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(2)) 