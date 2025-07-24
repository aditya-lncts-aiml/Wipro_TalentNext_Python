'''
Q1) WAP to add a key and value to a dictionary.
sample dictionary : {0:10, 1:20}
Expected Result : {0: 10, 1: 20, 2: 30}
'''

dict = {0: 10, 1: 20}
print(f"original dictionary: {dict}")
dict[2] = 30
print(f"after adding a new key and value: {dict}")

'''
Q2) WAP to conccatenate the following dictionaries to create a new one.
Sample dictionaies:
dic1 = {1: 10, 2: 20}  dic2 = {3: 30, 4: 40}  dic3 = {5: 50, 6: 60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)
print(f"concatenated dictionary: {new_dict}")

'''
Q3) WAP to check if a given key already exists in a dictionary
'''

def check_key_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

sample_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}
key_to_check = 2
print(f"Does the key {key_to_check} exist in the dictionary? {check_key_exists(sample_dict, key_to_check)}")

'''
Q4) WAP to iterate over a dictionary using for loop and print the keys alone, values alone, and both keys and values.
'''

sample_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}
print("Keys:")
for key in sample_dict.keys():
    print(key)
print("Values:")
for value in sample_dict.values():
    print(value)
print("Keys and Values:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")

'''
Q5) WAP to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are squares of the keys.
'''

squares_dict = {}
for i in range(1, 16):
    squares_dict[i] = i ** 2
print(f"Dictionary of squares from 1 to 15: {squares_dict}")

'''
Q6) WAP to sum all the values in a dictionary, considering the values will be int types.
'''

def sum_dict_values(dictionary):
    total = 0
    for value in dictionary.values():
        total += int(value)
    return total

sample_dict = {1: 10, 2: 20, 3: 30}
print(f"Sum of all values in the dictionary: {sum_dict_values(sample_dict)}")