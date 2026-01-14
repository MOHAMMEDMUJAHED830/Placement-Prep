# Q1. Basic Tuple Operations
# Problem: Create tuple (5, 10, 15, 10, 20) and print:

# First element
# Last element
# Slice from index 1 to 3

t = (5,10,15,10,20)
print(t[0])
print(t[-1])
print(t[1:4])


# Q3. Swapping using Tuple

# Scenario: Do variables a aur b ki values swap karo bina third variable use kiye.
# Input: a = 10, b = 20
# Expected Output:
# text

# Before Swap: a=10, b=20
# After Swap: a=20, b=10

a = 10
b = 20
print("Before Swap: a =", a, ", b =", b)
a, b = b, a 
print("After Swap: a =", a, ", b =", b)

# Q3. Count Occurrences
# Problem: Count how many times 10 appears in (5, 10, 15, 10, 20)

# Input: (5, 10, 15, 10, 20) and find 10
# Output: 2

t = (5,10,15,10,20)
f = 10
count = 0
for i in t:
    if i == f:
        count += 1
print(f"{f} appears {count} times in the tuple.")  

# Q4. List ↔ Tuple Conversion
# Problem: Convert [1,2,3,4] to tuple, then back to list
# Input: [1,2,3,4]
# Output:
# text
# Tuple: (1, 2, 3, 4)
# Back to list: [1, 2, 3, 4]

l = [1,2,3,4]
t = tuple(l)
print("Tuple:", t)
l = list(t)
print("Back to list:", l)

# Q5. Finding Max without max()
# Scenario: Man lo max() function band hai. Apne aap sabse bada number dhundo.
# Input: t = (12, 5, 45, 7)
# Expected Output: 45

t = (12, 5, 45, 7)
m = t[0]
for i in t:
    if i > m:
        m = i
print(m)

# Q6. Tuple Unpacking
# Problem: Unpack ("Mujahed", 8.8, "CSE") into variables

# Input: ("Mujahed", 8.8, "CSE")
# Output: Name: Mujahed, CGPA: 8.8, Branch: CSE

t = ("Mujahed" , 8.8, "CSE")
n , g , b = t[0], t[1], t[2]
print("Name:", n, ", CGPA:", g, ", Branch:", b)

# Q7. Unique Elements in Order
# Problem: From [1,2,2,3,1,4,3], make tuple (1,2,3,4) preserving order

# Input: [1,2,2,3,1,4,3]
# Output: (1, 2, 3, 4)

# using set 
l = [1,2,2,3,1,4,3]
l = tuple(set(l))
print(l)

# using loop 
l = [1,2,2,3,1,4,3]
ul = []
for i  in l:
    if i not in ul:
        ul.append(i)
t = tuple(ul)
print(t)

# Q9. Find Common Elements
# Problem: Find common in [1,2,3,4] and [3,4,5,6]

# Input: [1,2,3,4] and [3,4,5,6]
# Output: {3, 4}

a = [1,2,3,4]
b = [3,4,5,6]
c = []
for i in a:
    if i in b:
        c.append(i)
print(set(c))

# Q10. Check Subset
# Problem: Is {1,2} a subset of {1,2,3,4}?

# Input: {1,2} and {1,2,3,4}
# Output: True

a = {1,2}
b = {1,2,3,4}
print(a.issubset(b))

# Q10. Union (All Elements)

# Scenario: Do lists ke saare elements nikaalo, duplicates hat jaayein.
# Input: a = {1, 2}, b = {3, 4}
# Expected Output: {1, 2, 3, 4}

a = {1,2}
b = {3,4}
print(a.union(b))

# Q12. First Repeating Element
# Problem: Find first repeat in [5,1,4,2,1,3]

# Input: [5,1,4,2,1,3]
# Output: 1

a = [5,1,4,2,1,3]
for i in a :
    if a.count(i) > 1:
        print(i)
        break

# Q13. Common Characters Check
# Problem: Do "hello" and "world" share any character?

# Input: "hello" and "world"
# Output: True (common letters: o, l)

s1 = "hello"
s2 = "world"
print(bool(set(s1) & set(s2)))

# Skills Tracker (Real-world Use)
# Problem: Find skills you have vs need
# my_skills = {"python", "sql"}
# job_skills = {"python", "dsa", "sql", "git"}
# Input: my_skills and job_skills
# Output:
# text
# Have: {'python', 'sql'}
# Need: {'dsa', 'git'}

m = {"python", "sql"}
j = {"python", "dsa", "sql", "git"}
print("Have:", m)
print("Need:", j - m)






