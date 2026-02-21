import sys

N, M = map(int, sys.stdin.readline().split())
arr = list()
arr.append([0] * (N + 1))

arr_sum = list([0] * (N + 1) for _ in range(N + 1))

for _ in range(N):
    arr.append([0] + list(map(int, sys.stdin.readline().split())))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        arr_sum[i][j] = (
            arr[i][j] + arr_sum[i][j - 1] + arr_sum[i - 1][j] - arr_sum[i - 1][j - 1]
        )

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    res = (
        arr_sum[x2][y2]
        - arr_sum[x2][y1 - 1]
        - arr_sum[x1 - 1][y2]
        + arr_sum[x1 - 1][y1 - 1]
    )
    print(res)
