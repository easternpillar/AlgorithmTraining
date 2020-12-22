# Problem:
# Print in order from the given number to 0.

# My Solution:
N = int(input())
for i in range(N, -1, -1):
    print(i, end=" ")
