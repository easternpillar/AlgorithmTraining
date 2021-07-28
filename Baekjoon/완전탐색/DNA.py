# Problem:
# Reference: https://www.acmicpc.net/problem/1969

# My Solution:
import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
dna = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = ""
distance = 0
for zipped in list(zip(*dna)):
    counter = Counter(zipped).most_common()
    counter.sort(key=lambda x: (-x[1], x[0]))
    for i in range(len(counter)):
        if i == 0:
            answer += counter[i][0]
        else:
            distance += counter[i][1]
print(answer)
print(distance)
