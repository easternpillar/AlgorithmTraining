# Problem:
# Given connected ladders, return the minimum addition of ladders that makes it come down to the original position.
# Condition(s):
# 1. Ladders can not be set sequentially.

# My Solution: Denied.
# import copy
# from collections import deque
# import sys
#
#
# def downladder(ladder, vertical, horizontal):
#     for i in range(vertical):
#         ladder_num = i
#         for j in range(horizontal):
#             if ladder[j][ladder_num] == 1:
#                 ladder_num += 1
#             elif ladder_num - 1 >= 0 and ladder[j][ladder_num - 1] == 1:
#                 ladder_num -= 1
#         if i != ladder_num:
#             return False
#     return True
#
#
# n, m, h = map(int, list(input().split()))
# l = [[0 for i in range(n)] for j in range(h)]
#
# for _ in range(m):
#     for a, b in [list(map(int, input().split()))]:
#         l[a - 1][b - 1] = 1
#
# q = deque([[l, 0, [0, 0]]])
# while q:
#     temp = q.popleft()
#
#     if temp[1] > 3:
#         break
#
#     if downladder(temp[0], n, h):
#         print(temp[1])
#         sys.exit()
#     else:
#         i = temp[2][0]
#         j = temp[2][1]
#         while i < h:
#             while j < n:
#                 if (j - 1 >= 0 and temp[0][i][j - 1] == 1) or (j + 1 <= n - 1 and temp[0][i][j + 1] == 1):
#                     j += 1
#                     continue
#                 if temp[0][i][j] == 0 and j + 1 <= n - 1:
#                     tmp_ladder = copy.deepcopy(temp[0])
#                     tmp_ladder[i][j] = 1
#                     q.append([tmp_ladder, temp[1] + 1, [i, j]])
#                 j += 1
#             i += 1
#             j = 0
#
# print(-1)

ans = 4
n, m, h = map(int, input().split())
a = [[0] * n for _ in range(h)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x - 1][y - 1] = 1


def ladder():
    for i in range(n):
        k = i
        for j in range(h):
            if a[j][k]:
                k += 1
            elif k > 0 and a[j][k - 1]:
                k -= 1
        if i != k:
            return False
    return True


def solve(cnt, x, y):
    global ans
    if ans <= cnt:
        return
    if ladder():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n - 1):
            if a[i][j]:
                j += 1
            else:
                a[i][j] = 1
                solve(cnt + 1, i, j + 2)
                a[i][j] = 0


solve(0, 0, 0)
print(ans if ans < 4 else -1)
