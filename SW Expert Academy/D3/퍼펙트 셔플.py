# Problem:
# Given a card deck, print the order after perfect shuffle.

# My Solution:
from collections import deque
import math

for i in range(int(input())):
    N = int(input())
    d = input().split()
    d1, d2 = d[:int(math.ceil(N / 2))], d[int(math.ceil(N / 2)):]
    q1 = deque(d1)
    q2 = deque(d2)
    print("#{}".format(i + 1), end=' ')

    while q1 or q2:
        if q1:
            print(q1.popleft(), end=' ')
        if q2:
            print(q2.popleft(), end=' ')
    print()
