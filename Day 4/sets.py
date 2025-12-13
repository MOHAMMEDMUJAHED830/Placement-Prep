# Q8. Remove duplicates from:
# nums = [10, 20, 10, 30, 20, 40]
# Print the unique values (any order is fine).

l = [10, 20, 10, 30, 20, 40]
s = set(l)
print("Unique values:", s)

# Q9. Find common elements between:
# a = [1, 2, 3, 4], b = [3, 4, 5, 6]

a = [1, 2, 3, 4] 
b = [3, 4, 5, 6]
c = set(a).intersection(set(b))
print(f"common elements are : {c}")

# Q10. Check whether {1, 2} is a subset of {1, 2, 3, 4}.

a = {1, 2}
b = {1, 2, 3, 4}
s = a.issubset(b)
print(f"Is {a} a subset of {b}? : {s}")

# Q11. For sets A={1,2,3} and B={3,4,5} print:
# union
# intersection
# A - B
# symmetric difference

a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("A - B:", a.difference(b))
print("Symmetric Difference:", a.symmetric_difference(b))

# Q12. Find the first repeating element in a list using a set:
# arr = [5, 1, 4, 2, 1, 3]
# Expected output: 1 (because it’s the first element that repeats when scanning left to right)


a = [5, 1, 4, 2, 1, 3]
s = set()
first_repeating = None
for i in a:
    if i in s:
        first_repeating = i
        break
    s.add(i)
print("First repeating element:", first_repeating)

# Q13. Check if two strings share any common character using sets:
# s1="hello", s2="world"
# Output: True (common letters exist)

a = "hello"
b = "world"
c = set(a).intersection(set(b))
print("Common letters:", c)
if c != set():
    print("True (common letters exist)")
else:
    print("False (no common letters)")

# Q14. Mini-task: Skills tracker using sets
# my_skills = {"python", "sql"}
# job_skills = {"python", "dsa", "sql", "git"}

m = {"python", "sql"}
j = {"python", "dsa", "sql", "git"}
i = m.intersection(j)
print("You have the following required skills:", i)
mi = j.difference(m)
print("You need to learn the following skills:", mi)





