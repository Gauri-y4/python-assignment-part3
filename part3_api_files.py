# PART 3: FILE I/O, APIs & EXCEPTION HANDLING
# Product Explorer & Error-Resilient Logger
import requests
from datetime import datetime
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
print()
print()
print()

# TASK 3: EXCEPTION HANDLING

print("TASK 3: Exception Handling")
print()
# Part A — Guarded Calculator
print("Part A — Guarded Calculator")
print()
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"
# Test
print("Safe Divide Tests:")
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))
print()
print()

# Part B — Guarded File Reader
print("Part B — Guarded File Reader")
print()
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")
print("Reading existing file:")
print(read_file_safe(r"C:\Users\cvsat\OneDrive\Desktop\python_notes.txt"))
print()
print("Reading missing file:")
read_file_safe("ghost_file.txt")
print()
print()

# Part C — Robust API Calls
print("Part C — Robust API Calls")
print()
try:
    url = "https://dummyjson.com/products?limit=20"
    response = requests.get(url, timeout=5)
    data = response.json()
    print("API fetched successfully")
except requests.exceptions.ConnectionError:
    print("Connection failed. Please check your internet.")
except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")
except Exception as e:
    print("Error:", e)
print()
print()

# Part D — Input Validation Loop
print("Part D — Input Validation Loop")
print()
while True:
    user_input = input("Enter a product ID to look up (1–100), or 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
    # Validation
    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    product_id = int(user_input)
    if product_id < 1 or product_id > 100:
        print("Please enter a number between 1 and 100.")
        continue
    try:
        url = f"https://dummyjson.com/products/{product_id}"
        response = requests.get(url, timeout=5)
        if response.status_code == 404:
            print("Product not found.")
        else:
            data = response.json()
            print(f"{data['title']} - ${data['price']}")
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print("Error:", e)
print()
print()
print()

# TASK 4: LOGGING TO FILE
print("TASK 4: Logging To File")
print()
# Function for log errors
def log_error(context, error_type, message):
    with open(r"C:\Users\cvsat\OneDrive\Desktop\error_log.txt", "a", encoding="utf-8") as f:
        time = datetime.now()
        f.write(f"[{time}] ERROR in {context}: {error_type} — {message}\n")
print()
# Trigger ConnectionError
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except requests.exceptions.ConnectionError as e:
    log_error("fetch_products", "ConnectionError", str(e))
print()
# Trigger HTTP 404
response = requests.get("https://dummyjson.com/products/999", timeout=5)
if response.status_code != 200:
    log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")
print()
# Read and print log file
print("Error Log Contents:\n")

with open(r"C:\Users\cvsat\OneDrive\Desktop\error_log.txt", "r", encoding="utf-8") as f:
    print(f.read())
