def first_last(num):
    print("for the numbers {} equivalence of first and last is: {}".format(num, num[0] == num[-1]))


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

first_last(numbers_x)
first_last(numbers_y)

"""
Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

Given:

numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False
"""

