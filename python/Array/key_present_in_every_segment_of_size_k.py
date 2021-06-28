"""
Given an array arr[] and size of array is n and one another key x, and give you a segment size k.
The task is to find that the key x present in every segment of size k in arr[].
"""

def key_is_present(arr, size, k, x):
    """
        Check if a key is present in every segment of size k in an array
    :param arr: Array
    :param size: Size of the aray
    :param k: segment size
    :param x: Key
    :return: True/False
    """
    key_flag = False
    i = 0
    while i < size:
        j = 0
        segment_flag = False
        while j < k and i+j < size:
            print(arr[i + j])
            if arr[i + j] == x:
                segment_flag = True
                break
            j += 1
        print(segment_flag)
        if segment_flag:
            key_flag = True
        else:
            key_flag = False
            break
        i += k
    return key_flag


if __name__ == '__main__':
    arr = [5, 8, 7, 12, 14, 3, 9]
    k = 2
    x = 8
    key_present = key_is_present(arr, len(arr), k, x)
    if key_present:
        print("Yes present")
    else:
        print("Not present")


