# Given a string S, c1 and c2. Replace character c1 with c2 and c2 with c1.

"""
Examples:
    Input : str = 'grrksfoegrrks'
        c1 = e, c2 = r
    Output : geeksforgeeks

    Input : str = 'ratul'
            c1 = t, c2 = h
    Output : rahul
"""

if __name__ == '__main__':
    str = 'grrksfoegrrks'
    c1 = 'e'
    c2 = 'r'
    print("".join((map(lambda x: c1 if x == c2 else(c2 if x == c1 else x), str))))
    print("".join([(lambda x: c1 if x == c2 else(c2 if x == c1 else x))(x) for x in str]))
