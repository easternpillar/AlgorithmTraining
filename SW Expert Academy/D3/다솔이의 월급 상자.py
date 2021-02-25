# Problem:
# Given the scores in the box and the probabilities of picking that score, print the average.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    tot = 0
    print("#{}".format(i + 1), end=" ")
    for j in range(N):
        p, x = map(float, input().split())
        tot += p * x
    print(tot)
