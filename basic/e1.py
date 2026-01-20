"""
Given two integer numbers, write a Python program to return their product only if 
the product is equal to or lower than 1000. Otherwise, return their sum.
"""


def multisum(x,y):
    return x*y if x*y <= 1000 else x+y

# a,b = input("enter two numbers: ").split()

a,b = map(int, input("enter two numbers: ").split())

# print(multisum(int(a), int(b)))

print(multisum(a, b))