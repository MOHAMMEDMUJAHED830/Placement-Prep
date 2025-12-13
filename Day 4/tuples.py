# Q1. Create a tuple t = (5, 10, 15, 10, 20) and print:
# first element
# last element
# slice from index 1 to 3 (inclusive of 1, exclusive of 4)

t = (5, 10, 15, 10, 20 )
print("First element:", t[0])
print("Last element:", t[-1])
print("Slice from index 1 to 3:", t[1:4])

# Q2. Swap two variables a=10, b=20 using tuple unpacking (no temp variable).

a = 10 
b = 20 
a, b = (b, a)
print("After swapping: a =", a, ", b =", b)

# Q3. Count how many times 10 occurs in the tuple (5, 10, 15, 10, 20).

t = (5, 10, 15, 10, 20)
c = t.count(10)
print("Count of 10 in the tuple:", c)

# Q4. Convert lst = [1, 2, 3, 4] to a tuple, then convert that tuple back to a list.

l = [1, 2, 3, 4]
t = tuple(l)
print("Tuple:", t)
l2 = list(t)
print("List:", l2)

# Q5. Find the maximum element in a tuple without using max():
# (12, 3, 45, 7, 19)

t = (12, 3, 45, 7, 19)
m = t[0]
for i in t:
    if i > m:
        m = i
print("Maximum element in the tuple:", m)

# Q6. Unpack this tuple and print in a sentence:

info = ("Mujahed", 8.8, "CSE(AI&ML)")
name, gpa, department = info
print(f"{name} has a GPA of {gpa} and studies in the {department} department.")

# Q7. Given data = [1, 2, 2, 3, 1, 4, 3], create a tuple of unique elements preserving order
# Output should be: (1, 2, 3, 4)

a = [1, 2, 2, 3, 1, 4, 3]
u = []
for i in a:
    if i not in u:
        u.append(i)
t = tuple(u)
print("Tuple of unique elements:", t)

# Q8. Try to change an element in a tuple and catch the error using try-except.

t = (1, 2, 3)
try:
    t[1]= 5
except TypeError as e:
    print("Error:", e)

