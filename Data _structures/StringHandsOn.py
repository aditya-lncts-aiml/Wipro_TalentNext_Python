'''
Q1) WAP to count the number of upper and lower case letters in a string.
'''

def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

sample_string = "Hello World"
upper_count, lower_count = count_case(sample_string)
print(f"Upper case letters: {upper_count}, Lower case letters: {lower_count}")

'''
Q2) WAP that will check whether a given string is palindrome or not.
'''
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

sample_string = "abacaba"
print(f"Is the string '{sample_string}' a palindrome? {is_palindrome(sample_string)}")

'''
Q3) Given a string, return a new string made of n copies of the first 2 chars of the original string 
where n is the length of the string. The string length will be  >= 2.
If input is "Wipro", the output should be "WiWiWiWi".
'''

def repeat_first_two_chars(s):
    if len(s) < 2:
        return ""
    first_two_chars = s[:2]
    return first_two_chars * len(s)
sample_string = "Wipro"
result = repeat_first_two_chars(sample_string)
print(f"Result of repeating first two chars: {result}")

'''
Q4) Given a string, if the first or last chars are 'x', return the string without those 'x'
characters, else return the string unchanged.
If the input is "xHix", the output should be "Hi".
'''
def remove_x(s):
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    return s
sample_string = "xHix"
result = remove_x(sample_string)
print(f"String after removing 'x' from start and end: {result}")

'''
Q5) Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
You may assume that n is between 0 and the length of the string inclusive. For example
If the input is "Wipro" and 3, then the output should be "propropro".
'''

def repeat_last_n_chars(s, n):
    if n < 0 or n > len(s):
        return ""
    last_n_chars = s[-n:]
    return last_n_chars * n
sample_string = "Wipro"
n = 3
result = repeat_last_n_chars(sample_string, n)
print(f"Result of repeating last {n} chars: {result}")