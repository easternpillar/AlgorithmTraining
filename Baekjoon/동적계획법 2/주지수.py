# Problem:
# Given a two-dimensional array of natural numbers, print the sum of the areas.

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
terri = []
for _ in range(N):
    terri.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            terri[i][j] += terri[i][j - 1]
        elif j == 0:
            terri[i][j] += terri[i - 1][j]
        else:
            terri[i][j] += terri[i - 1][j] + terri[i][j - 1] - terri[i - 1][j - 1]

K = int(sys.stdin.readline().rstrip())
for i in range(K):
    sr, sc, er, ec = map(int, sys.stdin.readline().split())

    if sr == 1 and sc == 1:
        print(terri[er - 1][ec - 1])
    elif sr == 1:
        print(terri[er - 1][ec - 1] - terri[er - 1][sc - 2])
    elif sc == 1:
        print(terri[er - 1][ec - 1] - terri[sr - 2][ec - 1])
    else:
        print(terri[er - 1][ec - 1] - terri[er - 1][sc - 2] - terri[sr - 2][ec - 1] + terri[sr - 2][sc - 2])
