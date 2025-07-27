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