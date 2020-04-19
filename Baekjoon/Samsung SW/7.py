# Problem:
# Given the workable period and a schedule that has the times and the prices, return the maximum revenue.
# Condition(s):
# 1. N+1 day is not workable.

# My Solution:
from collections import deque

N = int(input())
work_pay = []
max_pay = [0] * N

for _ in range(N):
    work_pay.append(list(map(int, input().split())))

for i in range(N - 1, -1, -1):  # 뒤에서부터  다이나믹 프로그래밍
    day = work_pay[i][0]
    pay = work_pay[i][1]

    if day > N - i:  # 남은 기간보다 상담일이 길 경우
        if i != N - 1:
            max_pay[i] = max_pay[i + 1]  # 이전 최댓값 저장
        continue

    if i == N - 1:  # 마지막 날 하루짜리 상담
        max_pay[i] = pay
    elif i + day == N:  # 현재 일을 시작하면 정확히 마지막에 끝나는 경우
        max_pay[i] = max(pay, max_pay[i + 1])
    else:
        # 현재 일을 맡을 경우 or 맡지 않을 경우
        max_pay[i] = max(pay + max_pay[i + day], max_pay[i + 1])

print(max_pay[0])