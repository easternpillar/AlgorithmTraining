# Problem:
# Reference: https://www.acmicpc.net/problem/17626

# My Solution:
import sys

n = int(sys.stdin.readline().rstrip())
dp = [i for i in range(n + 1)]
dp[0] = 0

for i in range(2, int(n**0.5+1)):
    for j in range(i**2, n+1):

        if j - i ** 2 < 0:
            continue
        dp[j] = min(dp[j], dp[j - i ** 2] + 1)

print(dp[n])

# Other Solution(s):
# n = int(sys.stdin.readline().rstrip())
# min_sum = 4
# for a in range(int(n ** 0.5), int((n // 4) ** 0.5), -1):
#     if a * a == n:
#         min_sum = 1
#         break
#     else:
#         temp = n - a * a
#         for b in range(int(temp ** 0.5), int((temp // 3) ** 0.5), -1):
#             if a * a + b * b == n:
#                 min_sum = min(min_sum, 2)
#                 continue
#             else:
#                 temp = n - a * a - b * b
#                 for c in range(int(temp ** 0.5), int((temp // 2) ** 0.5), -1):
#                     if n == a * a + b * b + c * c:
#                         min_sum = min(min_sum, 3)
#
# print(min_sum)
