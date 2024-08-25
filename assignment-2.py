# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

# solution to assignment
# TASK 1: creating an empty list: my_list
my_list = []
print(f'created an empty list: my_list {my_list}')

# TASK 2: appending values to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f'appended values to my_list {my_list}')

# or using a for loop to append the data
# value = 10
# for x in range(4):
#     my_list.append(value)
#     value += 10
    
# print(my_list)

# TASK 3: inserting the value 15 as second position : 1
my_list.insert(1, 15)   # 1 rep index and 15 rep value
print(f'inserting the value 15 on the second position in the list {my_list}')

# TASK 4: extending a list with another list [50, 60, 70]
another_list = [50, 60, 70]
my_list.extend(another_list)
print(f'extended my_list with another list {my_list}')

# TASK 5: Removing the last element from my_list.
remove_item = my_list.pop(-1)
print(f'removed the last value in my_list {my_list}')
print(f'removed value is: {remove_item}')

# TASK 6: sorting my list in ascending order
my_list.sort(reverse=False)
print(f'sorted list: {my_list}')

# TASK 8: Find and print the index of the value 30 in my_list.
print(f'index of value 30 is : {my_list.index(30)}')