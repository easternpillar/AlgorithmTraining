# Problem:
# Given a positive integer, print the integer cube root of it.
# Condition(s):
# 1. Print -1 if there is no integer cube root.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    print("#{}".format(i + 1), end=" ")

    flag = False
    for j in range(1, int(N ** (1 / 3)) + 2):
        if j ** 3 == N:
            print(j)
            flag = True

    if not flag:
        print(-1)
