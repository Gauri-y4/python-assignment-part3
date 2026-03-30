# PART 3: FILE I/O, APIs & EXCEPTION HANDLING
# Product Explorer & Error-Resilient Logger
import requests

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

# TASK 2: API Integration
url = "https://dummyjson.com/products?limit=20"
response = requests.get(url)
data = response.json()
products = data["products"]
print("ID | Title | Category | Price | Rating")
print("----------------------------------------------------")
print()
for p in products:
    print(f"{p['id']} | {p['title']} | {p['category']} | ${p['price']} | {p['rating']}")
print()
print()
filtered = []
for p in products:
    if p["rating"] >= 4.5:
        filtered.append(p)
filtered.sort(key=lambda x: x["price"], reverse=True)
print("Filtered & Sorted Products (Rating >= 4.5):")
print()
for p in filtered:
    print(f"{p['title']} - ${p['price']} (Rating: {p['rating']})")
print()
print()
print("Laptop Products: ")
print()
url2 = "https://dummyjson.com/products/category/laptops"
response2 = requests.get(url2)
data2 = response2.json()
laptops = data2["products"]
for p in laptops:
    print(f"{p['title']} - ${p['price']}")
print()
print()
print("POST Request: ")
print()
new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"}
response3 = requests.post("https://dummyjson.com/products/add",json=new_product)
print(response3.json())
