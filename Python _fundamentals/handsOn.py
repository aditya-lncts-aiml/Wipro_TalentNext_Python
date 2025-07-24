'''
Q1) Write a program to check if a given number is Positive, Negative or Zero.
'''
num = float(input("Enter a number: "))
if num > 0: 
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

'''
Q2) Write a program to check if a given number is Even or Odd.
'''
num = int(input("Enter a number: "))
if num%2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

'''
Q3) Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 10 == num2 % 10:
    print(True)
else:
    print(False)

'''
Q4) Write a program to print numbers from 1 to 10 in a single row with one tab space
'''
for i in range(1, 11):
    print(i, end="\t")

'''
Q5) Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
'''
for i in range(24, 58, 2):
    print(i, end="\n")

'''
Q6) Write a program to check if a given number is prime or not.
'''
num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
elif num == 2:
    is_prime = True
else:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number.")

'''
Q7) Write a program to print prime numbers between 10 and 99.
'''
import math
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
for num in range(10, 100):
    if is_prime(num):
        print(num, end=" ")


'''
Q8) Write a program to print the sum of all the digits of a given number.
'''
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print(f"{sum_of_digits}")

'''
Q9. Write a program to reverse a given number and print.
'''
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"{reversed_num}")

'''
Q10) Write a program to find if the given number is palindrom or not.
'''
num = int(input("Enter a number: "))
reversed_num = 0
original_num = num
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")

