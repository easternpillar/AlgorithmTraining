# Problem:
# Reference: https://www.acmicpc.net/problem/1316

# My Solution:
import sys
from collections import defaultdict


def check(string):
    temp = list(string)
    dic = defaultdict(bool)
    prev = -1
    for c in temp:
        if dic[c]:
            if prev == c:
                continue
            else:
                return False
        else:
            dic[c] = True
        prev = c
    return True


answer = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    string = sys.stdin.readline().rstrip()
    if check(string):
        answer += 1

print(answer)
