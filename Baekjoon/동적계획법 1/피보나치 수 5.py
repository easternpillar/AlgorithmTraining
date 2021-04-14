# Problem:
# Print the nth value of the fibonacci sequence.

# My Solution:
import sys

fibo = [0 for _ in range(21)]
fibo[1] = 1
fibo[2] = 1
for i in range(3, 21):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
n = int(sys.stdin.readline().rstrip())
print(fibo[n])
