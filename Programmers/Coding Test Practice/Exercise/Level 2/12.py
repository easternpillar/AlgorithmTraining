# Problem:
# Given a list of numbers, return the LCM.

# My Solution:
def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def solution(arr):
    while True:
        if len(arr) == 1:
            return arr[0]
        a = arr.pop()
        b = arr.pop()
        arr.append((a * b) // gcd(a, b))
