n = int(input("How many numbers to add? "))
total = 0
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    total += num

print(f"The total sum is: {total}")