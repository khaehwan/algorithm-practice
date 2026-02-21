import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr_sum = [0]
arr_rem = [0] * M
sum = 0
count = 0

for num in arr:
    sum = (sum + num) % M
    if sum == 0:
        count += 1
    arr_rem[sum] += 1
    arr_sum.append(sum)


for i in range(M):
    if arr_rem[i] > 1:
        count += (arr_rem[i] * (arr_rem[i] - 1)) // 2

print(count)
