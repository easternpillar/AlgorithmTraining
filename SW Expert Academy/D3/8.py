# Problem:
# Given the income of n people, print the number of people with less than average income.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    incomes = list(map(int, input().split()))
    avg = sum(incomes) / N
    cnt = 0
    for ic in incomes:
        if ic <= avg:
            cnt += 1
    print("#{} {}".format(i + 1, cnt))
