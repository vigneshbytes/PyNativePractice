
while True :
    n = input("enter original number : ")    
    if n.isdigit():
        break
    else:
        print("enter number only. try again \n")

if n == n[::-1]:
    print("Yes. given number is palindrome number")
else:
    print("No. given number is NOT a palindrome number")





"""
Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
"""