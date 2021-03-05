# Problem:
# Given a list of scores, print the mode value.

# My Solution:
from collections import Counter

T = int(input())
for i in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    print("#{}".format(N), end=" ")
    cnt = Counter(scores)
    print(cnt.most_common()[0][0])
