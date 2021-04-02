# Problem:
# Given the N size chess board, print the number of cases where n queens cannot attack each other.

# My Solution:
from collections import deque


def possible(li, idx):
    target_row = len(li)
    for i in range(len(li)):
        row = i
        col = li[i]
        if idx == col:
            return False
        elif abs(idx - col) == target_row - row:
            return False
    return True


def nqueen(n):
    q = deque([[i] for i in range(n)])
    cnt = 0
    while q:
        pop = q.popleft()
        if len(pop) == n:
            cnt += 1
        for i in range(n):
            if possible(pop, i):
                temp = pop[:]
                temp.append(i)
                q.append(temp)
    return cnt


answer = []

for i in range(int(input())):
    N = int(input())
    answer.append(nqueen(N))

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
