"""
Given an input string, write a function that returns the Run Length Encoded string for the input string.

For example, if the input string is ‘wwwwaaadexxxxxx’, then the function should return ‘w4a3d1e1x6’.

Examples:
    Input  :  str = 'wwwwaaadexxxxxx'
    Output : 'w4a3d1e1x6'
"""
from collections import OrderedDict

if __name__ == '__main__':
    input = "wwwwaaadexxxxxx"
    dt = OrderedDict.fromkeys(input, 0)
    for ch in input:
        dt[ch] = dt[ch] + 1
    res = ''
    for key, value in dt.items():
        res = res + key + str(value)
    print(res)