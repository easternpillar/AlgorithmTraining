# Problem:
# Given 7 integers, print the number with the 5th largest sum of 3 integers.

# My Solution:
from itertools import combinations

T = int(input())
for i in range(T):
    num_list = list(map(int, input().split()))
    print("#{}".format(i + 1), end=" ")

    p_list = list(combinations(num_list, 3))
    sums = []
    for p in p_list:
        sums.append(sum(p))
    sums = list(set(sums))
    sums.sort(reverse=True)

    print(sums[4])
