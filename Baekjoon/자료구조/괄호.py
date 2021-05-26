# Problem:
# Reference: https://www.acmicpc.net/problem/9012

# My Solution:
import sys

answer = []
for _ in range(int(sys.stdin.readline().rstrip())):
    string = list(sys.stdin.readline().rstrip())
    tot = 0
    flag = True
    for c in string:
        if c == '(':
            tot += 1
            continue
        elif c == ')':
            if tot == 0:
                answer.append("NO")
                flag = False
                break
            tot -= 1
    if not flag:
        continue
    if tot > 0:
        answer.append("NO")
    else:
        answer.append("YES")

for a in answer:
    print(a)
