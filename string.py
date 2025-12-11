# Problem 6: Reverse a string.

a = "Python"
r_a = a[::-1]
print("The reversed string is:", r_a)

# Problem 7: Check if a word is palindrome (same forwards and backwards).

a = "madam"
if a == a[::-1]:
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome.")
a = "hello"
if a == a[::-1]:
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome.")

# Problem 8: Count vowels in a string.

a = "Hello World"
v = "aeiouAEIOU"
count = 0
for char in a:
    if char in v:
        count += 1
print("The number of vowels in the string is:", count)

# Problem 9: Convert first letter of each word to uppercase.

a = "hello world python"
u = a.title()
print("The string with first letter of each word capitalized is:", u)

# Problem 10: Remove all spaces from a string.

a = "H e l l o   W o r l d"
n_a = a.replace(" ", "")
print("The string after removing all spaces is:", n_a)


