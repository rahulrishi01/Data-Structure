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
    return s_s_metrix


def min_subset_sum_diff(arr):
    sum = 0
    for i in arr:
        sum += i
    size = len(arr)
    s_s_metrix = solve_subset_sum(arr, sum, size)
    subset_vector = []
    for i in range(sum+1):
        if s_s_metrix[size][i]:
            subset_vector.append(i)
    min_diff = 99999
    for i in range(int(len(subset_vector)/2)):
        min_diff = min(min_diff, sum - 2*subset_vector[i])
    return min_diff


if __name__ == '__main__':
    arr = [1, 6, 11, 5, 4]
    print(min_subset_sum_diff(arr))
