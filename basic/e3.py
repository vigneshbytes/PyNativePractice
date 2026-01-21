"""
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
"""

str = input("enter a string")

for i in range(len(str)):
    if i%2 == 0:
        print(str[i])

