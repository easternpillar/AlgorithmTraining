# Problem:
# Reference: https://www.acmicpc.net/problem/2470

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
fluid = list(map(int, sys.stdin.readline().split()))
fluid.sort()
left = 0
right = len(fluid) - 1
mini = 2000000000
idx1 = left
idx2 = right
while left < right:
    summ = fluid[left] + fluid[right]

    if mini >= abs(summ):
        mini = abs(summ)
        idx1 = left
        idx2 = right

    if summ < 0:
        left += 1
    else:
        right -= 1

print(fluid[idx1], fluid[idx2])
