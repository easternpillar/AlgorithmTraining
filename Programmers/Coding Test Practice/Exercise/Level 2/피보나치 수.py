# Problem:
# Return the remainder that the nth number of the Fibonacci sequence is divided by 1234567.

# My Solution:
def solution(n):
    fib = [0, 1]
    for i in range(n - 1):
        fib.append(fib[-1] + fib[-2])

    return fib[-1] % 1234567
