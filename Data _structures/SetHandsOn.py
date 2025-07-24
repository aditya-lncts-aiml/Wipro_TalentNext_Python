'''
Q1) WAP to remove a given item from the set.
'''
sample_set = {1, 2, 3, 4, 5}
item_to_remove = 3
if item_to_remove in sample_set:
    sample_set.remove(item_to_remove)
    print(f"Item {item_to_remove} removed from the set: {sample_set}")
else:
    print(f"Item {item_to_remove} not found in the set: {sample_set}")

'''
Q2) WAP to create an intersection of sets.
'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_set = set1.intersection(set2)
print(f"Intersection of {set1} and {set2}: {intersection_set}")

'''
Q3) WAP to create an union of sets.
'''

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Union of {set1} and {set2}: {union_set}")

'''
Q4) WAP to find the maximum and minimum value in a set.
'''
sample_set = {10, 20, 30, 40, 50}
max_value = max(sample_set)
min_value = min(sample_set)
print(f"Maximum value in the set: {max_value}")
print(f"Minimum value in the set: {min_value}")