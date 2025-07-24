'''
Q1) WAP to print the 4th element fron first ands 4th element from last in a tuple.
'''
tuple_data = (10, 20, 30, 40, 50, 60, 70, 80)
fourth_element = tuple_data[3]
fourth_from_last_element = tuple_data[-4]
print(f"4th element: {fourth_element}, 4th from last element: {fourth_from_last_element}")

'''
Q2) WAP to check whether an element exists in a tuple or not.
'''
def check_element_exists(tup, element):
    return element in tup

sample_tuple = (10, 20, 30, 40, 50)
element_to_check = 30
print(f"Does the element {element_to_check} exist in the tuple? {check_element_exists(sample_tuple, element_to_check)}")

'''
Q3) WAP to convert a list into a tuple.
'''

sample_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(sample_list)
print(type(converted_tuple))

'''
Q4) WAP to find the index of an item in a tuple.
'''

def find_index(tup, item):
    try:
        return tup.index(item)
    except ValueError:
        return -1  # Return -1 if the item is not found
sample_tuple = (10, 20, 30, 40, 50)
item_to_find = 30
index_of_item = find_index(sample_tuple, item_to_find)
if index_of_item != -1:
    print(f"The index of {item_to_find} in the tuple is: {index_of_item}")
else:
    print(f"{item_to_find} is not found in the tuple.")

'''
Q5) WAP to replace last value of tuples in a list of 100.
Sample list: [(10, 20, 30), (40, 50, 60), (70, 80, 90)] 
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
'''
sample_list_of_tuples = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
for i in range(len(sample_list_of_tuples)):
    sample_list_of_tuples[i] = sample_list_of_tuples[i][:-1] + (100,)
print(f"Updated list of tuples: {sample_list_of_tuples}")