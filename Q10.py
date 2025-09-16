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