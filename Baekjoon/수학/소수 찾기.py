# Problem:
# https://www.acmicpc.net/problem/1978

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0
for num in nums:
    if num == 1:
        continue
    flag = True
    for i in range(2, int((num ** 0.5)) + 1, 1):
        if num % i == 0:
            flag = False
            break
    if flag:
        answer += 1

print(answer)
