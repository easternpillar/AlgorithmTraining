# Problem:
# Reference: https://www.acmicpc.net/problem/11365

# My Solution:
import sys

answer = []
while True:
    code = sys.stdin.readline().rstrip()
    if code == "END":
        break
    else:
        code = list(code)
        code.reverse()
        answer.append("".join(code))

for a in answer:
    print(a)
