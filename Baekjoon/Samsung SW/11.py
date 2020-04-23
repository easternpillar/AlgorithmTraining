# Problem:
# Given a table of ability if some two persons are in a team, return the minimum gap of two teams.

# My Solution:
import itertools

n = int(input())
table = [list(map(int, list(input().split()))) for _ in range(n)]

p = []
for team in list(itertools.combinations([i for i in range(n)], n // 2)):
    p.append(team)

m = 9999
for i in range(len(p) // 2):
    t1 = t2 = 0
    team = p[i]
    for j in range(n // 2):
        member = team[j]
        for k in team:
            t1 += table[member][k]

    team = p[-i - 1]
    for j in range(n // 2):
        member = team[j]
        for k in team:
            t2 += table[member][k]
    m = min(m, abs(t1 - t2))

print(m)
