# Q7. Create a function that returns factorial of a number.

def f(n):
    if n==0 or n==1:
        return 1
    else:
        return n * f(n-1)

print(f(5))  # Output: 120

# Q8. Create a function is_prime(n) to check if number is prime.

def is_prime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False

# Q9. Create a function count_even_odd(lst) that returns count.

def count_even_odd(lst):
    e = 0
    o = 0
    for i in lst:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    return e, o
print(count_even_odd([1, 2, 3, 4, 5, 6]))  # Output: (3, 3)

# Q10. Function to reverse a string without using slicing.

def reverse_string(s):
    r = ""
    for char in s:
        r = char + r
    return r    
print(reverse_string("hello"))  # Output: "olleh"

# Q11. Function that filters and returns only positive numbers from a list.

def filter_positive_numbers(lst):
    positive_numbers = []
    for num in lst:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers
print(filter_positive_numbers([-10, 15, -20, 30, 0, -5, 25]))  # Output: [15, 30, 25]

# Q12. Function to check if two strings are anagrams.

def are_anagrams(a, b):
    c = 0
    for i in a:
        if i in b:
            c += 1
    if c == len(a) and len(a) == len(b):
        return True
    else:
        return False   

print(are_anagrams("listen", "silent"))  # Output: True