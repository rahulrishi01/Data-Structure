# A recursive solution to solve 0-1 knapsack problem

def solve_knapsack(wt, pft, W, n):
    return knapsack_0_1_recurvive(wt, pft, W, n)


def knapsack_0_1_recurvive(wt, pft, W, n):
    if W <= 0 or n <= 0:
        return 0
    if wt[n-1] <= W:
        return max(pft[n-1] + knapsack_0_1_recurvive(wt, pft, W - wt[n-1], n-1),
                   knapsack_0_1_recurvive(wt, pft, W, n-1))
    else:
        return knapsack_0_1_recurvive(wt, pft, W, n-1)


if __name__ == '__main__':
    weight = [1, 3, 4, 5]
    profit = [1, 4, 5, 7]
    knapsack_weight = 7
    print(solve_knapsack(weight, profit, knapsack_weight, len(profit)))
