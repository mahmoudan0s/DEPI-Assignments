### 2. Question: Repeat Characters in a String
##Description: Given a string, create a new string by repeating each character in the original string n times.
##Assume n is given and always a positive integer.
##Do not use if statements in your solution.

s = "abc"
n = 3

result = ""
for char in s:
    result += char * n

print(result)