# Problem:
# Reference: https://www.acmicpc.net/problem/2015

# My Solution:
import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
dic = defaultdict(int)

for i in range(1, N):
    arr[i] += arr[i - 1]

for i in range(N):
    if arr[i] == K:
        answer += 1
    answer += dic[arr[i] - K]
    dic[arr[i]] += 1
print(answer)
