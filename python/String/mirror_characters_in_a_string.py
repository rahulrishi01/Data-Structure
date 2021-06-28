# Given a string and a number N, we need to mirror the characters from N-th position up to the length of the string in
# the alphabetical order. In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.

"""
Example:
    Input : N = 3
        paradox
    Output : paizwlc
    We mirror characters from position 3 to end.

    Input : N = 6
            pneumonia
    Output : pnefnlmrz
"""


"""
Solution with map():

alpha_list = list('abcdefghijklmnopqrstuvwxyz')
alpha_list_reversed = list(reversed(alpha_list))

new_str = list(map(lambda x: alpha_list_reversed[alpha_list.index(x[1])] if x[0]>=N-1 else x[1], enumerate(my_str)))

print(''.join(new_str))
"""


def mirror_character(mc, n):
    al_chars = "abcdefghijklmnopqrstuvwxyz"
    mirror_chars = "zyxwvutsrqponmlkjihgfedcba"
    dict_char = dict(zip(al_chars, mirror_chars))

    prefix = mc[0: n-1]
    suffix = mc[n-1:]
    mirror = ""

    for i in suffix:
        mirror += dict_char[i]
    return prefix + mirror


if __name__ == '__main__':
    input_str = 'pneumonia'
    N = 6
    print(mirror_character(input_str, N))