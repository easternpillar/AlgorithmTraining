# Problem:
# Reference: https://www.acmicpc.net/problem/9934

# My Solution:
import sys

tree = []
K = int(sys.stdin.readline().rstrip())
buildings = [list(map(int, sys.stdin.readline().split()))]

while True:
    if not buildings[0]:
        break

    temp = []
    for building in buildings:
        length=len(building)
        print(building[length // 2], end=" ")
        temp.append(building[:length // 2])
        temp.append(building[length // 2 + 1:])
    print()
    buildings = temp[:]
