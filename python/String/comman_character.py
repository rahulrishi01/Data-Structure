# Given two strings, print all the common characters in lexicographical order.
# If there are no common letters, print -1. All letters are lower case.

# Example
"""
Input :
string1 : geeks
string2 : forgeeks
Output : eegks
Explanation: The letters that are common between
the two strings are e(2 times), k(1 time) and
s(1 time).
Hence the lexicographical output is "eegks"

Input :
string1 : hhhhhello
string2 : gfghhmh
Output : hhh
"""

from collections import Counter


def comman_chars(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    comman = c1 & c2
    if not len(comman):
        return -1
    else:
        return ''.join(sorted(list(comman.elements())))


if __name__ == '__main__':
    str1 = 'geeks'
    str2 = 'forgeeks'
    print(comman_chars(str1, str2))
