# Reference: https://www.acmicpc.net/problem/14889

import math
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
possible_team = []

for team in list(combinations([i for i in range(N)], N // 2)):
    possible_team.append(team)

min_stat_gap = math.inf
for i in range(len(possible_team) // 2):

    team = possible_team[i]
    stat_A = 0
    for j in range(N // 2):
        for k in team:
            stat_A += S[team[j]][k]

    team = possible_team[-i - 1]
    stat_B = 0
    for j in range(N // 2):
        for k in team:
            stat_B += S[team[j]][k]

    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))

print(min_stat_gap)
