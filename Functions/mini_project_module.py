def ispalindrome(name):
    name = name.replace(" ", "").lower()
    return name == name[::-1]

def count_the_vowels(name):
    vowels = "aeiou"
    count = 0
    name = name.lower()
    for char in name:
        if char in vowels:
            count += 1
    return count

def frequency_of_letters(name):
    frequency = {}
    name = name.replace(" ", "").lower()
    for char in name:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return ",".join([f"{char}-{count}" for char, count in frequency.items()])