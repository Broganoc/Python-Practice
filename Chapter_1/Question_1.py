# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


import string
import random

# initializing size of string
N = 7

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_letters, k=N))


def check_unique():
    temp = ""
    for char in res:
        if char not in temp:
            temp += char
    if res == temp:
        return res + " is unique"
    else:
        return res + " is not unique"


# checking uniqueness with help of other data structure
def check_unique_struct():
    for i in res:
        if res.count(i) > 1:
            return res + " is not unique"
    return res + " is unique"
