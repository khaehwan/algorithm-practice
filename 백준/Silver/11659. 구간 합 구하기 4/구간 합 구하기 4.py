import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr_sum = [0]
sum = 0

for num in arr:
    sum += num
    arr_sum.append(sum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    res = arr_sum[j] - arr_sum[i - 1]
    print(res)
