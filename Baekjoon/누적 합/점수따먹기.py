# Problem:
# Reference: https://www.acmicpc.net/problem/1749

# My Solution:
N, M = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(N)]
srr = [[0 for _ in range(M)] for _ in range(N)]
for i in range(M):
    srr[0][i] = arr[0][i]
for i in range(1, N):
    for j in range(M):
        srr[i][j] = srr[i - 1][j] + arr[i][j]
answer = max(max(arr[i]) for i in range(N))
for i in range(N - 1):
    for j in range(i + 1, N):
        temp = 0
        for k in range(M):
            val = srr[j][k] - srr[i][k]
            temp += val
            answer = max(answer, temp)
            if temp < 0:
                temp = 0
print(answer)
