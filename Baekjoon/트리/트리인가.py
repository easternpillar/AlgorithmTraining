# Problem:
# Reference: https://www.acmicpc.net/problem/6416

# My Solution:
import sys
from collections import defaultdict, Counter

idx = 0
while True:
    quit = sys.stdin.readline().rstrip().split()

    if quit:
        if int(quit[0]) < 0 and int(quit[1]) < 0:
            break

    indegree = defaultdict(int)
    temp = []
    temp += quit
    idx += 1
    while True:
        temp += list(map(int, sys.stdin.readline().rstrip().split()))

        if temp[-1] == 0 and temp[-2] == 0:
            break
    if len(temp) == 2:
        print("Case", idx, "is a tree.")
        continue

    for i in range(0, len(temp) - 2, 2):
        if temp[i] not in indegree.keys():
            indegree[temp[i]] = 0
        if temp[i + 1] not in indegree.keys():
            indegree[temp[i + 1]] = 0
        indegree[temp[i + 1]] += 1
    counter = Counter(indegree.values())

    if counter[0] != 1 or not (len(counter.keys()) <= 2 and sum(counter.keys()) == 1):
        print("Case", idx, "is not a tree.")
    else:
        print("Case", idx, "is a tree.")
