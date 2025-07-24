'''
Q1) WAP to create a list of 5 integers and display the list items. Access individual elements through index.
'''

integer_list = [10, 20, 30, 40, 50]
print("List of integers:", integer_list)

for i in range(len(integer_list)):
    print(f"Element at index {i}: {integer_list[i]}")

'''
Q2) WAP to append a new item to the end of the list.
'''
integer_list = [10, 20, 30, 40, 50]
print("Original list:", integer_list)
integer_list.append(60)
print("List after appending 60:", integer_list)

'''
Q3) WAP to reverse the order of items in the list.
'''

integer_list = [10, 20, 30, 40, 50]
print("Original list:", integer_list)
integer_list.sort(reverse=True)
print("List after reversing:", integer_list)

'''
Q4) WAP to print the number of occurrences of a specific item in the list.
'''

integer_list = [10, 20, 30, 20, 50, 20, 60, 10, 20]
item_to_count = int(input("Enter the item to count: "))
count = integer_list.count(item_to_count)
print(f"The item {item_to_count} occurs {count} times in the list.")


'''
Q5) WAP to append the items of list1 to list2 in the front.
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list2 = list1 + list2
print("List2 after appending items of List1 in front:", list2)

'''
Q6) WAP to insert a new element before the second element in the existing list.
'''

integer_list = [10, 20, 30, 40, 50]
print("Original list:", integer_list)
new_element = int(input("Enter a new element to insert before the second element: "))
integer_list.insert(1, new_element)
print("List after inserting the new element:", integer_list)

'''
Q7) WAP to remove the item from a specific index in the list.
'''

integer_list = [10, 20, 30, 40, 50]
print("Original list:", integer_list)
index_to_remove = int(input("Enter the index of the item to remove: "))
if 0 <= index_to_remove < len(integer_list):
    removed_item = integer_list.pop(index_to_remove)
    print(f"Removed item: {removed_item}")
else:
    print("Index out of range.")

'''
Q8) WAP to remove the first occurrence of a specific element from the list.
'''

integer_list = [10, 20, 30, 20, 50]
print("Original list:", integer_list)
item_to_remove = int(input("Enter the item to remove: "))
if item_to_remove in integer_list:
    integer_list.remove(item_to_remove)
    print(f"List after removing the first occurrence of {item_to_remove}:", integer_list)
else:
    print(f"Item {item_to_remove} not found in the list.")
