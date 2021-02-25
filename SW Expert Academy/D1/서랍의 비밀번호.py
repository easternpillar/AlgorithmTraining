# Problem:
# Given P and K, print out how many times you can fit P, starting with K.

# My Solution:
P, K = map(int, (input().split()))

print(P - K + 1)
