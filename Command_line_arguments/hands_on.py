'''
Q1) Write a program to accept two numbers as command line arguments and display their sum.
'''
from sys import argv

print("Sum of", argv[1], "and", argv[2], "is:", int(argv[1]) + int(argv[2]))

'''
Q2) Write a program to accept a welcome message through command line arguments and display the file
name along with the welcome message.
'''
from sys import argv
if len(argv) < 2:
    print("Usage: python welcome_message.py <your welcome message>")
else:
    filename = argv[0]
    message = ' '.join(argv[1:])
    print(f"Filename: {filename}")
    print(f"Welcome message: {message}")

'''
Q3) Write a program to accept 10 numbers through command line arguments and calculate the sum of prime
numbers among them.
'''
import math
from sys import argv
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    total = 0
    for num in numbers:
        if is_prime(num):
            total += num
    return total
sum_of_primes_list = [int(num) for num in argv[1:11]]
if len(argv) < 11:
    print("Please provide 10 numbers as command line arguments.")
else:
    print("Sum of prime numbers:", sum_of_primes(sum_of_primes_list))