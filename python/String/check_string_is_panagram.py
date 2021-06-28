"""
Given a string, check if the given string is pangram or not.
Examples:

Input : The quick brown fox jumps over the lazy dog
Output : The string is a pangram

Input : geeks for geeks
Output : The string is not pangram
"""
from string import ascii_lowercase as asc_le


def check_panagram(s):
    if (set(asc_le) - set(s)) == set([]):
        print("The string is a pangram")
    else:
        print("The string is not pangram")


if __name__ == '__main__':
    s = 'The quick brown fox jumps over the lazy dog'
    check_panagram(s)