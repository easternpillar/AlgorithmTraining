# Problem:
# Reference: https://www.acmicpc.net/problem/1620

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
dic = dict()
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    dic[str(i + 1)] = temp
    dic[temp] = str(i + 1)

for i in range(M):
    print(dic[sys.stdin.readline().rstrip()])
