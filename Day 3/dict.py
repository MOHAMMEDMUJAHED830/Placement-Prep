# Q1. Create a dictionary storing 3 students and their marks.

studets_marks = {
    "mohammed" : 100,
    "khan" : 98,
    "syed" : 95,
    }
print(studets_marks)

# Q2. Count frequency of each character in a string.

a = "hello"
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
print(b)

# Q3. Merge two dictionaries into one.

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
c = {**a, **b}
print(c)

# Q4. Create a dictionary with numbers from 1 to 5 and their squares.

a = {i : i**2 for i in range(1, 6)}
print(a)

# Q5. Get all keys and values separately from a dictionary.

a = {'name': 'Alice', 'age': 25, 'city': 'New York'}
k= a.keys()
v = a.values()
print("Keys:", k)
print("Values:", v)

# Q6. Convert 2 lists into a dictionary.

a = ['name', 'age', 'city']
b = ['Alice', 25, 'New York']
c = {zip(a, b)}
print(c)

