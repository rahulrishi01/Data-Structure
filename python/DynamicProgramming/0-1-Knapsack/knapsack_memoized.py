# A memoized solution to solve 0-1 knapsack problem
profit_matrix = []


def solve_knapsack(wt, pft, W, n):
    global profit_matrix
    profit_matrix = [[-1 for x in range(W+1)] for y in range(n+1)]
    return knapsack_0_1_memoized(wt, pft, W, n)


def knapsack_0_1_memoized(wt, pft, W, n):
    if W <= 0 or n <= 0:
        return 0
    if profit_matrix[n][W] != -1:
        return profit_matrix[n][W]
    if wt[n-1] <= W:
        profit_matrix[n][W] = max(pft[n-1] + knapsack_0_1_memoized(wt, pft, W - wt[n-1], n-1),
                   knapsack_0_1_memoized(wt, pft, W, n-1))
    else:
        profit_matrix[n][W] = knapsack_0_1_memoized(wt, pft, W, n-1)
    return profit_matrix[n][W]


if __name__ == '__main__':
    weight = [1, 3, 4, 5]
    profit = [1, 4, 5, 7]
    knapsack_weight = 7
    print(solve_knapsack(weight, profit, knapsack_weight, len(profit)))
