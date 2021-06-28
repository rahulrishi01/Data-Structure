"""
We are given a string and we need to reverse words of given string ?

Examples:

Input : str = "geeks quiz practice code"
Output : str = "code practice quiz geeks"
"""

if __name__ == '__main__':
    input = "geeks quiz practice code"
    print(' '.join((input.split(' '))[::-1]))
