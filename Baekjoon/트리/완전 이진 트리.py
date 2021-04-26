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
        print(building[len(building) // 2], end=" ")
        temp.append(building[:len(building) // 2])
        temp.append(building[len(building) // 2 + 1:])
    print()
    buildings = temp[:]
