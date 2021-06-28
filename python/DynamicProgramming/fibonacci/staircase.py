def solve_staircase(n, x):
    if n == 0:
        return 1
    count_ways = []
    count_ways.insert(0, 1)
    for i in range(1, n+1):
        total = 0
        for j in range(1, x+1):
            if i - j >= 0:
                total += count_ways[i-j]
        count_ways.insert(i, total)
    return count_ways[n]


if __name__ == '__main__':
    num_stairs = 4
    num_steps = 2  # 1 or 2 or 3
    print(solve_staircase(num_stairs, num_steps))
