# Problem:
# Given two sorted arrays, print the merged array being sorted.

# My Solution:
import sys
import heapq

answer = []
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.extend(B)
heapq.heapify(A)
while A:
    print(heapq.heappop(A), end=" ")

# Problem:
# Given two sorted arrays, print the merged array being sorted.

# Other Solution:
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# A = list(map(int, sys.stdin.readline().split()))
# B = list(map(int, sys.stdin.readline().split()))
# A.extend(B)
# for a in sorted(A):
#     print(a, end=" ")