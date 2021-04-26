# Problem:
# Print the number of M strings that are given as inputs that are included in the set S.

# My Solution:
import sys

N, M = map(int, sys.stdin.readline().split())
string_set = set()
cnt = 0
for i in range(N):
    string_set.add(sys.stdin.readline().rstrip())
for i in range(M):
    if sys.stdin.readline().rstrip() in string_set:
        cnt += 1

print(cnt)
