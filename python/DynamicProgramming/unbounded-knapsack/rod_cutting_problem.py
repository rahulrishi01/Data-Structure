# A memoized solution to solve rod cutting problem
profit_matrix = []


def solve_rod_cutting(rod_len, pft, W, n):
    global profit_matrix
    profit_matrix = [[0 for x in range(W+1)] for y in range(n+1)]
    return rod_cutting_dp(rod_len, pft, W, n)


def rod_cutting_dp(rod_len, pft, W, n):

    for i in range(1, n+1):
        for j in range(1, W+1):
            if rod_len[i-1] <= j:
                profit_matrix[i][j] = max(pft[i-1] + profit_matrix[i][j - rod_len[i-1]],
                           profit_matrix[i-1][j])
            else:
                profit_matrix[i][j] = profit_matrix[i-1][j]
    return profit_matrix[n][W]


if __name__ == '__main__':
    length = [1, 2, 3, 4, 5, 6, 7, 8]
    profit = [1, 5, 8, 9, 10, 17, 17, 20]
    rod_length = 8
    print(solve_rod_cutting(length, profit, rod_length, len(profit)))
