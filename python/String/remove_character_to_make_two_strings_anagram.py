from collections import Counter

"""
Given two strings in lowercase, the task is to make them Anagram. The only allowed operation is to remove a character
from any string. Find minimum number of characters to be deleted to make both the strings anagram?
If two strings contains same data set in any order then strings are called Anagrams.
"""

# Examples
"""
Input : str1 = "bcadeh" str2 = "hea"
Output: 3
We need to remove b, c and d from str1.

Input : str1 = "cddgk" str2 = "gcd"
Output: 2

Input : str1 = "bca" str2 = "acb"
Output: 0
"""


def count_of_chars_remove_to_get_anagram(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    comman_chars = counter1 & counter2
    comman_chars_length = len(list(comman_chars.elements()))
    total_chars = len(str1) + len(str2)
    return total_chars - (2 * comman_chars_length)


if __name__ == '__main__':
    s1 = 'bca'
    s2 = 'acb'
    print(count_of_chars_remove_to_get_anagram(s1, s2))
