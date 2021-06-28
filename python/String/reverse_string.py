# Python string library does’nt support the in-built “reverse()”
# Python code to reverse a string


def reverse_string1(string):
    return string[::-1]


def reverse_string2(string):
    st = ""
    for i in string:
        st = i + st
    return st


def reverse_string3(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string3(string[1:]) + string[0]


def reverse_string4(string):
    return "".join(reversed(string))


if __name__ == '__main__':
    str = "reversestring"
    print(reverse_string4(str))

