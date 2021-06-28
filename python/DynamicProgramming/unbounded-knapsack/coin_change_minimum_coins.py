# A DP solution to solve coin change problem
profit_matrix = []
INT_MAX = 9999999


def solve_coin_change(coin, total, n):
    global profit_matrix
    profit_matrix = [[0 for x in range(total+1)] for y in range(n+1)]
    for i in range(1, total+1):
        profit_matrix[1][i] = int(i/coin[0]) if i % coin[0] == 0 else INT_MAX
    return coin_change_dp(coin, total, n)


def coin_change_dp(coin, total, n):

    for i in range(2, n+1):
        for j in range(1, total+1):
            if coin[i-1] <= j:
                profit_matrix[i][j] = min((1 + profit_matrix[i][j - coin[i-1]]), profit_matrix[i-1][j])
            else:
                profit_matrix[i][j] = profit_matrix[i-1][j]
    return profit_matrix[n][total]


if __name__ == '__main__':
    coin = [1, 5, 6, 8]
    total = 11
    print(solve_coin_change(coin, total, len(coin)))
