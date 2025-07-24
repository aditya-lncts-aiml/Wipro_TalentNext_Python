'''Mini-Project1'''

'''
Write a Python function that accepts a hyphen-separated sequence of colors
as input and returns the colors in a hyphen-separated sequence after sorting
them alphabetically.

Constraint: All the colors will be completely in either lower case or upper case.

Sample input 1: green-red-yellow-black-white
Sample output 1: black-green-red-white-yellow

Sample input 2: PINK-BLUE-TAN-PURPLE
Sample output 2: BLUE-PINK-PURPLE-TAN
'''

def sort_colors(color_string):
    if color_string.islower():
        colors_string = color_string.lower()
    else:
        colors_string = color_string.upper()
    colors = colors_string.split('-')
    colors.sort()
    print(colors)
    return '-'.join(colors)
sample_input1 = "Green-red-yellow-black-white"
print(sort_colors(sample_input1))

sample_input2 = "PINK-BLUE-TAN-PURPLE"
print(sort_colors(sample_input2))


'''Mini-Project2'''

'''
Create a Python module with the following functions:

Function Name Task
ispalindrome(name) Given the user name as input, this function should
tell us whether the name is a palindrome or not.
count_the_vowels(name) Given the user name as input, this function should
tell us how many vowels are present in it.
frequency_of_letters(name) Given the user name as input, this function should
tell us how many times each letter appears in the
name.

Note: name will be completely in either lower case or upper case.

Import the module in another python script and test the functions by passing
appropriate inputs.

Sample input 1: bob
Sample output 1:
Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1


Sample input 2: marcel bentok tanaka
Sample output 2:
No it is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1, k-2
'''

import mini_project_module as mpm
print(f"Yes it is a palindrome." if mpm.ispalindrome("bob") else "No it is not a palindrome.")
print(f"No of vowels: {mpm.count_the_vowels('bob')}")
print(f"Frequency of letters: {mpm.frequency_of_letters('bob')}")