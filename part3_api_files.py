# PART 3: FILE I/O, APIs & EXCEPTION HANDLING
# Product Explorer & Error-Resilient Logger

# TASK 1: File Read & Write Basics 
#Part A: 
notes = ["Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."]

with open("python_notes.txt", "w", encoding="utf-8") as f:
    for line in notes:
        f.write(line + "\n")

print("Successfully written file.")
with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions make code reusable.\n")
    f.write("Topic 7: Python is easy to learn and use.\n")
print("Lines appended.")

#Part B:
#Reading File
with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print("Reading file content:")
print()
# numbered Lines
for i, line in enumerate(lines, 1):
    print(f"{i}. {line.strip()}")print()
#Total np. of lines in file
print("\nTotal number of lines:", len(lines))
print()
#Searching Keywords
keyword = input("\nEnter a keyword to search: ").lower()
found = False
for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True
if not found:
    print("No matching lines found.")
