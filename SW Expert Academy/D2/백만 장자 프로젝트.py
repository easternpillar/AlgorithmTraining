# Problem:
# Given the selling price of consecutive days, print out the maximum profit you can get.
# Condition(s):
# 1. You can only buy one per day.
# 2. You can sell it at any time.

# My Solution:
T = int(input())

for i in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    temp.insert(0, 10001)

    tot = 0
    max_idx = len(temp) - 1
    for j in range(len(temp) - 2, -1, -1):
        if temp[j] >= temp[max_idx]:
            tot -= sum(temp[j + 1:max_idx])
            tot += len(temp[j + 1:max_idx]) * temp[max_idx]
            max_idx = j

    print("#{} {}".format(i + 1, tot))
