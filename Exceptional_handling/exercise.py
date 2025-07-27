



# 1 Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
try:
    result = num1 / num2
    print("Result of division:", result)
except Exception as e:
    print("Error occurred:", e)




# # 2 Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.

try:
    num = int(input("Enter a number to check if it's prime: "))
    if num < 2:
        print(f"{num} is not a prime number.")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")
except ValueError:
    print("Error: Please enter a valid integer.")



# # 3 Write a program to accept the file name to be opened from the user, if file exists print the contents of the file in title case or else handle the exception and print an error message.

try:
    file_name = input("Enter the file name: ")
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents.title())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error occurred:", e)




# # 4 Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.

numbers = [12, -7, 5, 0, -3, 8, 14, -2, 6, -10]

try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    if value > 0:
        print("The number at index", index, "is positive.")
    elif value < 0:
        print("The number at index", index, "is negative.")
    else:
        print("The number at index", index, "is zero.")
except IndexError:
    print("Error: Invalid index. Please enter an index from 0 to 9.")
except ValueError:
    print("Error: Please enter a valid integer.")


