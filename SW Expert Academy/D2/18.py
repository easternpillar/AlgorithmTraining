# Problem:
# Given two dates, print how many days are the difference.

# My Solution:
T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    d = 0
    print("#{}".format(i + 1), end=" ")
    d += sum(days[m1 - 1:m2 - 1])
    d -= d1 - d2
    print(d + 1)
