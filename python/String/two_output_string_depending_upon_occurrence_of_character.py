# Given an input string str[], generate two output strings. One of which consists of those character which
# occurs only once in input string and second which consists of multi-time occurring characters.
# Output strings must be sorted.
from collections import Counter

"""
Example:
    Input : str = "geeksforgeeks"
    Output : String with characters occurring once:
    "for".
    String with characters occurring multiple times:
    "egks"
    
    Input : str = "geekspractice"
    Output : String with characters occurring once:
    "agikprst"
    String with characters occurring multiple times:
    "ce"
"""

if __name__ == '__main__':
    input_str = 'geekspractice'
    str_frq = Counter(input_str)
    freq_1_str = [key for (key, count) in str_frq.items() if count == 1]
    freq_str_other = [key for (key, count) in str_frq.items() if count > 1]
    freq_1_str.sort()
    freq_str_other.sort()
    print('Character occurs only once is: {}'.format(''.join(freq_1_str)))
    print('Multi-time occurring characters are: {}'.format(''.join(freq_str_other)))
