# Reference: https://www.acmicpc.net/problem/20922
import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

left = right = 0
dic = defaultdict(int)
dic[seq[left]] += 1
maxi = 0
while True:
    right += 1
    if right >= len(seq):
        maxi = max(maxi, right - left)
        break

    dic[seq[right]] += 1
    if dic[seq[right]] > K:
        maxi = max(maxi, right - left)

        while seq[left] != seq[right]:
            dic[seq[left]] -= 1
            left += 1
        dic[seq[left]] -= 1
        left += 1
print(maxi)
