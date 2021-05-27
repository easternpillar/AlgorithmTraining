# Problem:
# Print the n-th fibonacci number.

# My Solution:
import sys

fibo = [0 for _ in range(91)]
fibo[1] = 1
for i in range(2, len(fibo)):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

n = int(sys.stdin.readline().rstrip())
print(fibo[n])
