# Problem:
# Given the workable period and a schedule that has the times and the prices, return the maximum revenue.
# Condition(s):
# 1. N+1 day is not workable.

# My Solution:
N = int(input())
work_pay = []
max_pay = [0] * N

for _ in range(N):
    work_pay.append(list(map(int, input().split())))

for i in range(N - 1, -1, -1):
    day = work_pay[i][0]
    pay = work_pay[i][1]

    if day > N - i:
        if i != N - 1:
            max_pay[i] = max_pay[i + 1]
        continue

    if i == N - 1:
        max_pay[i] = pay
    elif i + day == N:
        max_pay[i] = max(pay, max_pay[i + 1])
    else:
        max_pay[i] = max(pay + max_pay[i + day], max_pay[i + 1])

print(max_pay[0])