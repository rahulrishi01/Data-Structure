# A DP solution to solve coin change problem
profit_matrix = []


def solve_coin_change(coin, total, n):
    global profit_matrix
    profit_matrix = [[0 for x in range(total+1)] for y in range(n+1)]
    for i in range(total+1):
        profit_matrix[0][i] = 0
    for i in range(n+1):
        profit_matrix[i][0] = 1
    return coin_change_dp(coin, total, n)


def coin_change_dp(coin, total, n):

    for i in range(1, n+1):
        for j in range(1, total+1):
            if coin[i-1] <= j:
                profit_matrix[i][j] = profit_matrix[i][j - coin[i-1]] + profit_matrix[i-1][j]
            else:
                profit_matrix[i][j] = profit_matrix[i-1][j]
    return profit_matrix[n][total]


if __name__ == '__main__':
    coin = [1, 2, 3]
    total = 5
    print(solve_coin_change(coin, total, len(coin)))
