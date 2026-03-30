# PART 3: FILE I/O, APIs & EXCEPTION HANDLING
# Product Explorer & Error-Resilient Logger

# TASK 1: File Read & Write Basics 
print("TASK 1: File Read & Write Basics ")
print()
# Part A:
notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."]
# using one file path everywhere
file_path = r"C:\Users\cvsat\OneDrive\Desktop\python_notes.txt"
# write
with open(file_path, "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")

print("Successfully written file.")
print()
# append
with open(file_path, "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions make code reusable.\n")
    f.write("Topic 7: Python is easy to learn and use.\n")
print("Lines appended.")
print()

# Part B:
# Reading File
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("Reading file content:")
print()
# numbered Lines
for i, line in enumerate(lines, 1):
    print(f"{i}. {line.strip()}")
print()
# Total no. of lines in file
print("Total number of lines:", len(lines))
print()
# Searching Keywords
keyword = input("\nEnter a keyword to search: ").lower()
found = False
for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True
if not found:
    print("No matching lines found.")
print()
print()
print()
