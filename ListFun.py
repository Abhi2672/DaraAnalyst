# Creating a list
my_list = [10, 20, 30, 40, 50]

# 1. Append an element
my_list.append(60)
print("After append:", my_list)

# 2. Extend a list
my_list.extend([70, 80])
print("After extend:", my_list)

# 3. Insert an element at a specific position
my_list.insert(2, 25)  # Insert 25 at index 2
print("After insert:", my_list)

# 4. Remove an element
my_list.remove(30)  # Removes the first occurrence of 30
print("After remove:", my_list)

# 5. Pop an element (default last element)
popped = my_list.pop()
print("Popped element:", popped)
print("After pop:", my_list)

# 6. Index of an element
index = my_list.index(40)
print("Index of 40:", index)

# 7. Count occurrences of an element
count = my_list.count(20)
print("Count of 20:", count)

# 8. Sort the list
my_list.sort()
print("Sorted list:", my_list)

# 9. Reverse the list
my_list.reverse()
print("Reversed list:", my_list)

# 10. Copy the list
copy_list = my_list.copy()
print("Copied list:", copy_list)

# 11. Clear the list
my_list.clear()
print("After clear:", my_list)

# 12. List comprehension (creating a new list)
squared_list = [x**2 for x in copy_list]
print("Squared list:", squared_list)

# 13. Check if an element is in the list
print("Is 50 in list?", 50 in copy_list)

# 14. Getting the length of the list
print("Length of list:", len(copy_list))

# 15. Min and Max values
print("Min value:", min(copy_list))
print("Max value:", max(copy_list))

# 16. Sum of all elements
print("Sum of list:", sum(copy_list))
