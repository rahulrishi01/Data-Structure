import math

def fibonacci_reverse(n):
    if n < 0:
        print("Incorrect input")
        return
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_reverse(n-1) + fibonacci_reverse(n-2)


def fibonacci_iterative(n):
    a0, a1 = 0, 1
    if n == 0:
        return a0
    if n == 1:
        return 1
    for i in range(2, n+1):
        sum = a0 + a1
        a0 = a1
        a1 = sum
    return sum


def fibonacci_math(n):
    # Fn = {[(√5 + 1)/2] ^ n} / √5
    phi = (1 + math.sqrt(5)) / 2
    return round(math.pow(phi, n)/math.sqrt(5))


def fibonacci_dp():
    pass


if __name__ == '__main__':
    n = 6
    print(fibonacci_reverse(n))
    print(fibonacci_iterative(n))
    print(fibonacci_math(n))