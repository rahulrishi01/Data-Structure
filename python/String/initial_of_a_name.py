"""
Given a name, print the initials of a name(uppercase) with last name(with first alphabet in uppercase) written in full
separated by dots.

Example:
    Input : geeks for geeks
    Output : G.F.Geeks

    Input : mohandas karamchand gandhi
    Output : M.K.Gandhi
"""

if __name__ == '__main__':
    s = "mohandas karamchand gandhi"
    d = s.split(' ')
    st = ''
    for i in range(len(d) - 1):
        print(d[i][0])
        st += (d[i][0]).upper() + '.'
    st += (d[-1]).title()
    print(st)