str_x = "Emma is good developer. Emma is a writer"

def counter(str, word):
    lstr = str.split()
    i = lstr.count(word)
    print(f"{word} appeared {i} times")

counter(str_x, "Emma")









"""
Exercise 7: Find the number of occurrences of a substring in a string
Write a Python code to find how often the substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times
"""