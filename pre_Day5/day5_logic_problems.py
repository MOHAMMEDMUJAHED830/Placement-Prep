# Q1. Factorial (Recursion)
# Input: 5
# Output: 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(factorial(num))

# Q2. Fibonacci (First n terms)
# Input: 6
# Output: 0 1 1 2 3 5

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
num_terms = 6
fibonacci(num_terms)
print("\n")

# Q3. Star Triangle
# Input: 4
# Output:
# text
# *
# **
# ***
# ****

a = 4
for i in range(1, a + 1):
    print("*" * i)
print("\n")

# Q4. Number Square
# Input: 3
# Output:
# text
# 111
# 222
# 333

n = 3
for i in range(1, n + 1):
    print(str(i) * n)
print("\n")

# Q5. Right Rotation
# Input: [1,2,3,4,5] and k=2
# Output: [4,5,1,2,3]

a = [1, 2, 3, 4, 5]
k = 2
for _ in range(k):
    a.insert(0, a.pop())
print("Right Rotated List:", a)
print("\n")

# Q6. Palindrome Number (Without string)
# Input: 121
# Output: True

a = 78687
b = a
r = 0
for i in range(len(str(a))):
    d = a % 10
    r = r * 10 + d
    a = a // 10
if r == b:
    print(f"{b} is a palindrome number")
else:
    print(f"{b} is not a palindrome number")
print("\n")

# Q7. Armstrong Number
# Input: 153
# Output: True

def is_armstrong(num):
    original = num
    digits = len(str(num))
    sum_cubes = 0
    while num > 0:
        digit = num % 10
        sum_cubes += digit ** digits
        num //= 10
    return original == sum_cubes

# Q8. GCD/HCF
# Input: 12, 18
# Output: 6

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Q9. LCM
# Input: 4, 6
# Output: 12

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Q10. Missing Number (1 to n)
# Input: [1,2,4,5] (n=5)
# Output: 3

def missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

# Q11. Binary to Decimal
# Input: "1010"
# Output: 10

def bin_to_dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

# Q12. Decimal to Binary
# Input: 10
# Output: "1010"

def dec_to_bin(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary

# Q13. Unique Element (XOR Trick)
# Input: [2,3,5,4,5,3,2]
# Output: 4

def unique_element(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

# Q14. Primes in Range
# Input: 1 to 20
# Output: 2 3 5 7 11 13 17 19

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(1, 21) if is_prime(x)]
print(primes)

# Q15. List Intersection
# Input: [1,2,3,4] and [3,4,5,6]
# Output: [3,4]

def intersection(l1, l2):
    return list(set(l1) & set(l2))


