# Problem Statement:
# Given binary array, find count of maximum number of consecutive 1’s present in the array.

# Example:
"""
Input  : arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}
Output : 4

Input  : arr[] = {0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1}
Output : 1
"""


def max_consec_1_in_arr(arr):
    max_len = -1
    count = 0
    for n in arr:
        if n == 1:
            count += 1
        else:
            count = 0
        if count > max_len:
            max_len = count
    return max_len


def max_consec_1_in_str(str):
    return max(map(len, str.split('0')))


if __name__ == '__main__':
    arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
    print(max_consec_1_in_arr(arr))
    str = '1100011111101010111'
    print(max_consec_1_in_str(str))
