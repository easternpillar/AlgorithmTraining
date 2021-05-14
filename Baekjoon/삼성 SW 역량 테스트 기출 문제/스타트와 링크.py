# Problem:
# Given a table of ability if some two persons are in a team, return the minimum gap of two teams.

# My Solution:
import itertools

n = int(input())
table = [list(map(int, list(input().split()))) for _ in range(n)]

answer = set()
for p in list(itertools.combinations([i for i in range(n)], n // 2)):
    t1 = t2 = 0
    for i in range(n):
        for j in range(i, n, 1):
            if i in p and j in p:
                t1 += table[i][j] + table[j][i]
            if i not in p and j not in p:
                t2 += table[i][j] + table[j][i]
    answer.add(abs(t1 - t2))
print(min(answer))
