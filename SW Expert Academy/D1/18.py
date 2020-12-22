# Problem:
# Print the value(s) multiplied by 2 from 1 to a given number of times.

# My Solution:
N = int(input())
for i in range(N + 1):
    print(2 ** i, end=" ")
