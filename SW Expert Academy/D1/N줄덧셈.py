# Problem:
# Given a number, print the sum of the numbers from 1 to the given number.

# My Solution:
N = int(input())
total = 0
for i in range(1, N + 1):
    total += i

print(total)
