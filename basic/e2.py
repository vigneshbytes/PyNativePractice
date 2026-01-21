"""
Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
"""

current = prev = 0;

for current in range(10):
    print(f"Current Number {current} Previous Number {prev}  Sum:  {current+prev}")
    prev = current

    