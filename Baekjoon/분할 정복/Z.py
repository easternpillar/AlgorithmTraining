# Problem:
# Reference: https://www.acmicpc.net/problem/1074

# My Solution: DENIED.
# import sys
#
#
# def dc(row, col, l):
#     global cnt
#     if l == 1:
#         if row == r and col == c:
#             print(cnt)
#             exit(0)
#         cnt += 1
#         return
#     else:
#         for i in range(row, row + l, l // 2):
#             for j in range(col, col + l, l // 2):
#                 dc(i, j, l // 2)
#
#
# N, r, c = map(int, sys.stdin.readline().split())
# cnt = 0
# dc(0, 0, 2 ** N)

N, r, c = list(map(int, input().split()))
result = 0
while N >= 1:
    temp = 2 ** (N - 1) - 1

    if r <= temp and c <= temp:

        N -= 1
        continue

    elif c > temp >= r:

        c = c - temp - 1
        result += (temp + 1) * (temp + 1)

    elif r > temp >= c:

        r = r - temp - 1
        result += (temp + 1) * (temp + 1) * 2

    else:

        c = c - temp - 1
        r = r - temp - 1
        result += (temp + 1) * (temp + 1) * 3
    N -= 1

print(result)
