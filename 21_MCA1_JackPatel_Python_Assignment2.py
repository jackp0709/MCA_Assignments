"""
*****************************  Question 1 ***********************************


from datetime import datetime

date1 = input("Enter first date in yyyy-mm-dd format: ")
date2 = input("Enter second date in yyyy-mm-dd format: ")

d1 = datetime.strptime(date1, "%Y-%m-%d")
d2 = datetime.strptime(date2, "%Y-%m-%d")

difference = d2 - d1

print("Difference in Dates : ",difference.days ,"days")

"""

"""
*****************************  Question 2 ***********************************


import time

seconds = time.time()

hours = int(seconds//3600)
minutes = int((seconds//60)%60)

print("Hours : ",hours," and Minutes : ",minutes)

"""

"""
*****************************  Question 3 ***********************************


from datetime import date,datetime

today = date.today()

DOB = input("Enter Birthdate in yyyy-mm-dd format: ")
dob = datetime.strptime(DOB, "%Y-%m-%d").date()

print("Your birthdate is : ",dob,", :)")

age_indays = (today- dob).days
print("You are ",age_indays," days old. :)")

years = today.year - dob.year
months = today.month - dob.month
days = today.day - dob.day

if days< 0:
    months -= 1
    days += 30

if months<0:
    years -=1
    months += 12

print("You are", years, "years and", months, "months and ",days," days old.")

"""

"""
*****************************  Question 4 ***********************************


import math

print("Angle   Sin       Cos       Tan")
print("--------------------------------")

angles = [0, 30, 45, 60, 90]

for angle in angles:
    rad = math.radians(angle)   

    sin_val = round(math.sin(rad), 3)
    cos_val = round(math.cos(rad), 3)

    
    if angle == 90:
        tan_val = "undefined"
    else:
        tan_val = round(math.tan(rad), 3)

    print(f"{angle:3}°   {sin_val:<8} {cos_val:<8} {tan_val}")

"""

"""
*****************************  Question 5 ***********************************


import random

print("Ten Random Numbers:\n")

for i in range(10):
    num = random.randint(1, 100)  
    print(num)

"""

"""
*****************************  Question 6 ***********************************


username = "Admin"
password = "123"

uname = input("Enter Username: ")
pwd = input("Enter your Password: ")

if(uname == username and pwd == password):
    print("Login Sucessfully!")
else:
    print("Invalid Username or Password")

"""

"""
*****************************  Question 7 ***********************************


import hashlib


username = "Admin"
password_hash = hashlib.sha256("123".encode()).hexdigest()

uname = input("Enter Username: ")
pwd = input("Enter Password: ")

pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()

if uname == username and pwd_hash == password_hash:
    print("Login successful!")
else:
    print("Invalid Username or Password")

"""

"""
*****************************  Question 8 ***********************************


import hashlib


username = "Admin"
password_hash = hashlib.sha256("123".encode()).hexdigest()

uname = input("Enter Username: ")
pwd = input("Enter Password: ")

pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()

if uname == username and pwd_hash == password_hash:
    print("Login successful!")
else:
    print("Invalid Username or Password")

"""

"""
*****************************  Question 9 ***********************************


import base64

original_string = "Hello$World"

string_bytes = original_string.encode("utf-8")

base64_bytes = base64.b64encode(string_bytes)

base64_string = base64_bytes.decode("utf-8")

print("Original String:", original_string)
print("Base64 Encoded:", base64_string)

"""

"""
s = "Hello World"
reversed_s = s[::-1]  
print("Reversed string:", reversed_s)
"""

"""
s = "Hello World"
print("Length of string:", len(s))
"""

"""
s = "Hello World"
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print("Character counts:", char_count)
"""

"""
s = "madam"
if s == s[::-1]:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
"""

"""
s = "Hello World"
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
"""

"""
s = "Hello World"
no_space = s.replace(" ", "")
print("Without spaces:", no_space)
"""

"""
s = "hello world"
print("Capitalized:", s.title())
"""

"""
s = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
"""

"""
s = "12345"
if s.isnumeric():
    print(s, "is numeric")
else:
    print(s, "is not numeric")
"""

"""
s = "Hello World"
substring = "World"
if substring in s:
    print(f"'{substring}' found in string")
else:
    print(f"'{substring}' not found")
"""



