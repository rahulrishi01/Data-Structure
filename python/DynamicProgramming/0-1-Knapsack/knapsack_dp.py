# A memoized solution to solve 0-1 knapsack problem
profit_matrix = []


def solve_knapsack(wt, pft, W, n):
    global profit_matrix
    profit_matrix = [[0 for x in range(W+1)] for y in range(n+1)]
    return knapsack_0_1_dp(wt, pft, W, n)


def knapsack_0_1_dp(wt, pft, W, n):

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                profit_matrix[i][j] = max(pft[i-1] + profit_matrix[i-1][j - wt[i-1]],
                           profit_matrix[i-1][j])
            else:
                profit_matrix[i][j] = profit_matrix[i-1][j]
    return profit_matrix[n][W]


if __name__ == '__main__':
    weight = [1, 3, 4, 5]
    profit = [1, 4, 5, 7]
    knapsack_weight = 7
    print(solve_knapsack(weight, profit, knapsack_weight, len(profit)))
