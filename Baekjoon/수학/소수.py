# Problem:
# Print the sum of prime numbers and minimum prime number between M and N.

# My Solution:
import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
mini = False
tot = 0
for i in range(M, N + 1):
    if i == 1:
        continue
    flag = True
    for j in range(2, int(i ** 0.5) + 1, 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        tot += i
        if not mini:
            mini = i
if tot == 0:
    print(-1)
else:
    print(tot)
    print(mini)
