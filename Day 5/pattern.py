# Q1. Factorial (Recursion): Write a function to find factorial using recursion.

def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n - 1)
num = int(input("Enter a number to find its factorial: "))
result = f(num)
print(f"The factorial of {num} is {result}")

# Q2. Fibonacci Series: Print first n terms (0, 1, 1, 2, 3, 5...).

def f(n):
    a, b = 0,1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
num = int(input("\nEnter the number of terms for Fibonacci series: "))
f(num)
print("\n")

# Q3. Star Pattern: Print a Right Angled Triangle (n=5).

n = 5
for i in range(1, n + 1):
    print("*" * i)

# Q4. Number Pattern: Print a square of numbers (111, 222, 333).

l = [111, 222, 333]
for i in l:
    for j in l:
        print(i, end=' ')
    print()

# Q5. List Rotation: Rotate a list [1,2,3,4,5] to the right by k steps.

l = [1, 2, 3, 4, 5]
k = 2
k = k % len(l)  # In case k is greater than length of list
rotated_list = l[-k:] + l[:-k]
print("Rotated List:", rotated_list)

# Q6. Palindrome Number: Check if 121 is a palindrome (without string conversion).

a = 121
o = a
r = 0
while a > 0:
    d = a % 10
    r = r * 10 + d
    a = a // 10
if o == r:
    print(f"{o} is a palindrome number")
else:
    print(f"{o} is not a palindrome number")

# Q7. Armstrong Number: Check if 153 is Armstrong number.

a = 153
o = a
s = 0
while a > 0:
    d = a % 10
    s += d ** 3
    a = a // 10
if o == s:
    print(f"{o} is an Armstrong number")
else:
    print(f"{o} is not an Armstrong number")

# Q8. GCD/HCF: Find the Greatest Common Divisor of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = 56
num2 = 98
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")

# Q9. LCM: Find the Least Common Multiple of two numbers.

def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)
num1 = 4
num2 = 5
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}")

# Q10. Find Missing Number: In a list of 1 to n, one number is missing. Find it.

def find_missing_number(arr, n):
    total = n * (n + 1) // 2
    sum_of_arr = sum(arr)
    return total - sum_of_arr
arr = [1, 2, 4, 5, 6]
n = 6
missing_number = find_missing_number(arr, n)
print(f"The missing number is {missing_number}")

# Q11. Binary to Decimal: Convert "1010" to 10.
binary_str = "1010"
decimal_value = int(binary_str, 2)
print(f"The decimal value of binary {binary_str} is {decimal_value}")

# Q12. Decimal to Binary: Convert 10 to "1010".

decimal_num = 10
binary_str = bin(decimal_num).replace("0b", "")
print(f"The binary representation of decimal {decimal_num} is {binary_str}")

# Q13. Check Prime: Check if 29 is a prime number.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = 29
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# Q13. Unique Elements: Given a list where every element repeats twice except one, find the unique one (Hint: Use XOR or Set).

def find_unique_element(arr):
    unique_element = 0
    for num in arr:
        unique_element ^= num
    return unique_element
arr = [2, 3, 5, 4, 5, 3, 2]
unique = find_unique_element(arr)
print(f"The unique element in the list is {unique}")

# Q14. Prime Numbers in Range: Print all primes between 1 and 100.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Prime numbers between 1 and 100 are:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=' ')
print()

# Q15. List Intersection: Find common elements in 3 sorted lists.

def intersection_of_three_lists(a, b, c):
    return list(set(a) & set(b) & set(c))
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 5, 7, 11]
list3 = [1, 3, 5, 9, 13]
common_elements = intersection_of_three_lists(list1, list2, list3)
print(f"Common elements in the three lists are: {common_elements}")




