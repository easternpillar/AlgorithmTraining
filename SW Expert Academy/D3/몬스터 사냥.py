# Problem:
# Given the damage, the level, the number of hits, print the total damage.
# 1. The damage of the next attack is D(1+n*L/100).

# My Solution:
T = int(input())
for i in range(T):
    print("#{}".format(i + 1), end=" ")
    D, L, N = map(int, input().split())
    print(int(N * D + D * L / 100 * ((N * (N - 1)) / 2)))
