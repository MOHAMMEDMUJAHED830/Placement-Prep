# Q1. Write to File

# Scenario: Create a file notes.txt and write "I am a CSE student" inside it.
# Input: String.
# Output: notes.txt file created in folder.

with open("notes.txt", "w") as file:
    file.write("I am a CSE student")
    print("notes.txt file created in folder.")

# Q2. Read from File

# Scenario: Read the content of notes.txt and print it.
# Input: notes.txt.
# Output: I am a CSE student.

with open("notes.txt", "r") as file:
    print(file.read())

# Q3. Append to File

# Scenario: Add "Learning Python for Placements" to the same file without deleting the first line.
# Output: File now has 2 lines.

with open("notes.txt", "a") as file:
    file.write("\nLearning Python for Placements")
    print("file now has 2 lines.")
with open("notes.txt", "r") as file:
    print(file.read())

# Q4. Count Words in File

# Scenario: Open any text file and count how many words are inside.
# Input: notes.txt.
# Output: 6 (approx).

with open("notes.txt", "r") as file:
    c = file.read()
    w = c.split()
    print("Number of words in file:", len(w))

# Q5. Safe File Open (Error Handling)

# Scenario: Try to open a file that doesn't exist. Use try-except so it prints "File not found" instead of crashing.
# Output: File not found.
try:
    with open("text.txt","r") as f:
        print(f.read())
except Exception as e:
    print("error is :", e)