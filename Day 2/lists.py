# Problem 1: Write a program to find the sum of all numbers in a list.

list = [10, 20, 30, 40]
sum = sum(list)
print("The sum of all numbers in the list is:", sum)

#or

list = [10, 20, 30, 40]
sum = 0
for i in list:
    sum += i
print("The sum of all numbers in the list is:", sum)

# Problem 2: Find the largest number in a list WITHOUT using max().

list = [45, 67, 23, 89, 12]
largest = list[0]
for i in range(len(list)):
    if list[i] > largest:
        largest = list[i]
print("The largest number in the list is:", largest)

# Problem 3: Count how many even numbers are in a list.

list = [1, 2, 3, 4, 5, 6]
even = 0
for i in list:
    if i % 2 == 0:
        even += 1
print("The count of even numbers in the list is:", even)

# Problem 4: Reverse a list WITHOUT using [::-1] or reverse().

list = [1, 2, 3, 4, 5]
r_list = []
for i in range(len(list)):
    r_list.insert(0, list[i])
print("The reversed list is:", r_list)

# Problem 5: Remove all duplicates from a list.

list = [1, 2, 2, 3, 4, 4, 5]
u_list = []
for i in list:
    if i not in u_list:
        u_list.append(i)
print("The list after removing duplicates is:", u_list)


