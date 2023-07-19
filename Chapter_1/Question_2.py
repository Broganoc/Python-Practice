# Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(string1, string2):
    # check if lengths are equal
    if len(string1) == len(string2):
        # reformat strings to list of characters
        res1 = ''.join(sorted(string1))
        res2 = ''.join(sorted(string2))

        if res1 == res2:
            return string2 + " is a permutation of " + string1

    return string2 + " is not a permutation of " + string1


