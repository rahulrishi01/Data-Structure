# Dynamic programming approach to solve subset sum problem
def solve_subset_sum(arr, sum, n):
    s_s_metrix = [[False for x in range(sum+1)] for y in range(n+1)]
    for i in range(n+1):
        s_s_metrix[i][0] = True
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                s_s_metrix[i][j] = s_s_metrix[i-1][j] or s_s_metrix[i-1][j - arr[i-1]]
            else:
                s_s_metrix[i][j] = s_s_metrix[i-1][j]
    return s_s_metrix[n][sum]


if __name__ == '__main__':
    arr = [2, 3, 7, 8, 10]
    sum = 30
    print(solve_subset_sum(arr, sum, len(arr)))
