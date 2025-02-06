# Welcome to Python Sripting


# Python Project List

| S.N | Project         | Description                                                                 |
|-----|-----------------|-----------------------------------------------------------------------------|
| 1   | [SystemStress](https://github.com/m14r41/Scripting4Hackers/tree/main/PYTHON/SystemStress)     | Scripts designed for system performance stress testing and benchmarking.  |
| 2   | [100 advanceSript.md](https://github.com/m14r41/Scripting4Hackers/blob/main/PYTHON/100%20advanceSript.md) | A markdown file containing 100 advanced scripting techniques and examples.  |


# Other Python Script Project

| S.N | Project Name | Description | Credit |
| --- | ------------ | ----------- | ------ |
| 1   | [PythonCode Tutorials (Ethical Hacking)](https://github.com/x4nth055/pythoncode-tutorials/tree/master/ethical-hacking) | Python tutorials for ethical hacking techniques. | [x4nth055](https://github.com/x4nth055) |
| 2   | [Ethical Hacking Tools in Python](https://github.com/x4nth055/ethical-hacking-tools-python) | Python tools for penetration testing and security. | [x4nth055](https://github.com/x4nth055) |


---

# Basics color in Python

```python

# Define color variables
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"

# Bold Colors
bold_black = "\033[1;30m"
bold_red = "\033[1;31m"
bold_green = "\033[1;32m"
bold_yellow = "\033[1;33m"
bold_blue = "\033[1;34m"
bold_magenta = "\033[1;35m"
bold_cyan = "\033[1;36m"
bold_white = "\033[1;37m"

# Background Colors
bg_black = "\033[40m"
bg_red = "\033[41m"
bg_green = "\033[42m"
bg_yellow = "\033[43m"
bg_blue = "\033[44m"
bg_magenta = "\033[45m"
bg_cyan = "\033[46m"
bg_white = "\033[47m"

# Reset color
reset = "\033[0m"

# Printing colors with their variables
print(f"{black}Black{reset}")
print(f"{red}Red{reset}")
print(f"{green}Green{reset}")
print(f"{yellow}Yellow{reset}")
print(f"{blue}Blue{reset}")
print(f"{magenta}Magenta{reset}")
print(f"{cyan}Cyan{reset}")
print(f"{white}White{reset}")

print(f"{bold_black}Bold Black{reset}")
print(f"{bold_red}Bold Red{reset}")
print(f"{bold_green}Bold Green{reset}")
print(f"{bold_yellow}Bold Yellow{reset}")
print(f"{bold_blue}Bold Blue{reset}")
print(f"{bold_magenta}Bold Magenta{reset}")
print(f"{bold_cyan}Bold Cyan{reset}")
print(f"{bold_white}Bold White{reset}")

print(f"{bg_black}Black Background{reset}")
print(f"{bg_red}Red Background{reset}")
print(f"{bg_green}Green Background{reset}")
print(f"{bg_yellow}Yellow Background{reset}")
print(f"{bg_blue}Blue Background{reset}")
print(f"{bg_magenta}Magenta Background{reset}")
print(f"{bg_cyan}Cyan Background{reset}")
print(f"{bg_white}White Background{reset}")

```

---

# Colors uning 'colorama' module.

```python
from colorama import Fore, Back, Style, init

# Initialize colorama (for Windows support)
init(autoreset=True)

# Printing colors with their variables
print(f"{Fore.BLACK}Black{Style.RESET_ALL}")
print(f"{Fore.RED}Red{Style.RESET_ALL}")
print(f"{Fore.GREEN}Green{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Yellow{Style.RESET_ALL}")
print(f"{Fore.BLUE}Blue{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}Magenta{Style.RESET_ALL}")
print(f"{Fore.CYAN}Cyan{Style.RESET_ALL}")
print(f"{Fore.WHITE}White{Style.RESET_ALL}")

print(f"{Fore.BLACK + Style.BRIGHT}Bold Black{Style.RESET_ALL}")
print(f"{Fore.RED + Style.BRIGHT}Bold Red{Style.RESET_ALL}")
print(f"{Fore.GREEN + Style.BRIGHT}Bold Green{Style.RESET_ALL}")
print(f"{Fore.YELLOW + Style.BRIGHT}Bold Yellow{Style.RESET_ALL}")
print(f"{Fore.BLUE + Style.BRIGHT}Bold Blue{Style.RESET_ALL}")
print(f"{Fore.MAGENTA + Style.BRIGHT}Bold Magenta{Style.RESET_ALL}")
print(f"{Fore.CYAN + Style.BRIGHT}Bold Cyan{Style.RESET_ALL}")
print(f"{Fore.WHITE + Style.BRIGHT}Bold White{Style.RESET_ALL}")

print(f"{Back.BLACK}Black Background{Style.RESET_ALL}")
print(f"{Back.RED}Red Background{Style.RESET_ALL}")
print(f"{Back.GREEN}Green Background{Style.RESET_ALL}")
print(f"{Back.YELLOW}Yellow Background{Style.RESET_ALL}")
print(f"{Back.BLUE}Blue Background{Style.RESET_ALL}")
print(f"{Back.MAGENTA}Magenta Background{Style.RESET_ALL}")
print(f"{Back.CYAN}Cyan Background{Style.RESET_ALL}")
print(f"{Back.WHITE}White Background{Style.RESET_ALL}")

```


# Top 100 Essential python sript


### 1. **Print Statement**
```python
print("Hello, World!")
```

### 2. **Variables**
```python
x = 10
name = "John"
```

### 3. **Data Types**
```python
integer = 5
float_num = 5.5
string = "Hello"
boolean = True
```

### 4. **Casting**
```python
int_num = int(3.5)
float_num = float(3)
str_num = str(3)
```

### 5. **String Concatenation**
```python
greeting = "Hello" + " " + "World"
```

### 6. **String Formatting**
```python
name = "Alice"
print(f"Hello, {name}!")
```

### 7. **String Methods**
```python
s = "hello world"
print(s.upper())  # Output: "HELLO WORLD"
```

### 8. **Multi-line Strings**
```python
text = '''This is 
a multi-line 
string.'''
```

### 9. **List Creation**
```python
fruits = ["apple", "banana", "cherry"]
```

### 10. **Accessing List Elements**
```python
print(fruits[0])  # Output: apple
```

### 11. **List Methods**
```python
fruits.append("orange")
fruits.remove("banana")
```

### 12. **List Slicing**
```python
subset = fruits[1:3]
```

### 13. **List Iteration**
```python
for fruit in fruits:
    print(fruit)
```

### 14. **List Comprehension**
```python
squares = [x**2 for x in range(5)]
```

### 15. **Tuple Creation**
```python
coordinates = (1, 2)
```

### 16. **Accessing Tuple Elements**
```python
print(coordinates[0])  # Output: 1
```

### 17. **Dictionary Creation**
```python
person = {"name": "Alice", "age": 25}
```

### 18. **Accessing Dictionary Elements**
```python
print(person["name"])  # Output: Alice
```

### 19. **Dictionary Methods**
```python
person["age"] = 26
```

### 20. **Set Creation**
```python
unique_numbers = {1, 2, 3}
```

### 21. **Set Operations**
```python
unique_numbers.add(4)
```

### 22. **Conditional Statements**
```python
if x > 10:
    print("x is greater than 10")
```

### 23. **If-Else Statement**
```python
if x == 10:
    print("Equal to 10")
else:
    print("Not equal to 10")
```

### 24. **Elif Statement**
```python
if x == 10:
    print("Equal to 10")
elif x == 5:
    print("Equal to 5")
```

### 25. **While Loop**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 26. **For Loop**
```python
for i in range(5):
    print(i)
```

### 27. **Break Statement**
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### 28. **Continue Statement**
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

### 29. **Function Definition**
```python
def greet(name):
    print(f"Hello, {name}!")
```

### 30. **Function Call**
```python
greet("Alice")
```

### 31. **Return Statement**
```python
def add(a, b):
    return a + b
```

### 32. **Lambda Function**
```python
square = lambda x: x**2
print(square(4))  # Output: 16
```

### 33. **Default Function Arguments**
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")
```

### 34. **Global Variables**
```python
x = 10

def print_x():
    global x
    print(x)
```

### 35. **Local Variables**
```python
def print_x():
    x = 10
    print(x)
```

### 36. **Recursion**
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### 37. **Reading from File**
```python
with open('file.txt', 'r') as file:
    content = file.read()
```

### 38. **Writing to File**
```python
with open('file.txt', 'w') as file:
    file.write("Hello, World!")
```

### 39. **Appending to File**
```python
with open('file.txt', 'a') as file:
    file.write("\nNew Line")
```

### 40. **File Existence Check**
```python
import os
if os.path.exists("file.txt"):
    print("File exists")
```

### 41. **Try-Except Block**
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 42. **Else in Try-Except**
```python
try:
    x = 1 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No error occurred")
```

### 43. **Finally Block**
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
```

### 44. **Importing Modules**
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### 45. **Aliasing Imports**
```python
import math as m
print(m.sqrt(16))  # Output: 4.0
```

### 46. **Handling JSON Data**
```python
import json
data = '{"name": "Alice", "age": 25}'
person = json.loads(data)
```

### 47. **Writing JSON Data**
```python
import json
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
```

### 48. **Creating a Class**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### 49. **Class Instantiation**
```python
person1 = Person("Alice", 25)
```

### 50. **Method in Class**
```python
class Person:
    def greet(self):
        print("Hello!")
```

### 51. **Inheritance**
```python
class Student(Person):
    def study(self):
        print("Studying...")
```

### 52. **Super Function**
```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

### 53. **Class Method**
```python
class Person:
    @classmethod
    def greet(cls):
        print("Hello from the class!")
```

### 54. **Static Method**
```python
class Person:
    @staticmethod
    def greet():
        print("Hello from the static method!")
```

### 55. **Module Creation**
```python
# In file mymodule.py
def greet():
    print("Hello, World!")
```

### 56. **List Indexing**
```python
arr = [1, 2, 3, 4]
print(arr[2])  # Output: 3
```

### 57. **List Length**
```python
arr = [1, 2, 3, 4]
print(len(arr))  # Output: 4
```

### 58. **Checking Item in List**
```python
if 3 in arr:
    print("3 is in the list")
```

### 59. **List Sorting**
```python
arr.sort()
```

### 60. **List Reversing**
```python
arr.reverse()
```

### 61. **Set Operations**
```python
a = {1, 2, 3}
b = {3, 4, 5}
union = a | b
```

### 62. **Dictionary Keys and Values**
```python
person = {"name": "Alice", "age": 25}
print(person.keys())   # Output: dict_keys(['name', 'age'])
```

### 63. **Dictionary Iteration**
```python
for key, value in person.items():
    print(key, value)
```

### 64. **Filter Function**
```python
arr = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, arr))
```

### 65. **Map Function**
```python
squared = list(map(lambda x: x**2, arr))
```

### 66. **Zip Function**
```python
names = ["Alice", "Bob"]
ages = [25, 30]
zipped = list(zip(names, ages))
```

### 67. **Enumerate Function**
```python
for index, value in enumerate(arr):
    print(index, value)
```

### 68. **Regular Expressions (Regex)**
```python
import re
pattern = r'\d+'
matches = re.findall(pattern, "There are 123 apples")
```

### 69. **Time Delay**
```python
import time
time.sleep(2)  # Sleep for 2 seconds
```

### 70. **Current Date and Time**
```python
import datetime
now = datetime.datetime.now()
print(now)
``

`

### 71. **Date Formatting**
```python
date_str = now.strftime("%Y-%m-%d")
```

### 72. **Working with Dates**
```python
from datetime import datetime
date = datetime(2024, 12, 25)
```

### 73. **Error Handling with Assert**
```python
assert 2 + 2 == 4
```

### 74. **Working with CSV Files**
```python
import csv
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
```

### 75. **Working with XML**
```python
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
```

### 76. **Command-Line Arguments**
```python
import sys
print(sys.argv)
```

### 77. **Logging**
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message.")
```

### 78. **Decorators**
```python
def decorator_function(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper
```

### 79. **Context Manager**
```python
class MyContext:
    def __enter__(self):
        print("Entering")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
```

### 80. **Threading**
```python
import threading
def print_numbers():
    for i in range(5):
        print(i)

t = threading.Thread(target=print_numbers)
t.start()
```

### 81. **AsyncIO**
```python
import asyncio
async def main():
    print("Hello")
asyncio.run(main())
```

### 82. **File Handling Context**
```python
with open("file.txt", "r") as file:
    data = file.read()
```

### 83. **Working with Bytes**
```python
data = b"Hello"
```

### 84. **Datetime Manipulations**
```python
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
```

### 85. **Working with CSV (Writing)**
```python
import csv
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
```

### 86. **File Compression**
```python
import zipfile
with zipfile.ZipFile('file.zip', 'w') as zipf:
    zipf.write('file.txt')
```

### 87. **Working with URLs**
```python
import urllib.request
response = urllib.request.urlopen('http://example.com')
```

### 88. **Unit Testing**
```python
import unittest
class TestMyFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
```

### 89. **Command Line Arguments**
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--number', type=int)
args = parser.parse_args()
```

### 90. **Working with Queues**
```python
from queue import Queue
q = Queue()
q.put(1)
item = q.get()
```

### 91. **Handling Environment Variables**
```python
import os
env_value = os.getenv('MY_VAR')
```

### 92. **Memory Management**
```python
import gc
gc.collect()
```

### 93. **Random Numbers**
```python
import random
random_num = random.randint(1, 100)
```

### 94. **Working with Networks**
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### 95. **Database Connectivity**
```python
import sqlite3
conn = sqlite3.connect('my_database.db')
```

### 96. **SQL Queries**
```python
cursor = conn.cursor()
cursor.execute("SELECT * FROM my_table")
```

### 97. **CRUD Operations**
```python
cursor.execute("INSERT INTO my_table (name) VALUES (?)", ('Alice',))
```

### 98. **Regex Substitution**
```python
import re
result = re.sub(r'\d+', 'number', 'abc123xyz')
```

### 99. **Sending Emails**
```python
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("your_email", "password")
```

### 100. **Sending HTTP Requests**
```python
import requests
response = requests.get('https://api.example.com')
```
