# Reference: https://www.acmicpc.net/problem/16918
import sys

R, C, N = map(int, sys.stdin.readline().split())
bombs = []
answer = [['.' for _ in range(C)] for _ in range(R)]
s = set()
time = 2
for i in range(R):
    temp = list(sys.stdin.readline().rstrip())
    for j in range(len(temp)):
        if temp[j] == 'O':
            bombs.append((i, j))

if N <= 1:
    while bombs:
        r, c = bombs.pop()
        answer[r][c] = 'O'
    for a in answer:
        print("".join(a))

elif N % 2 == 0:
    for _ in range(R):
        print('O' * C)

else:
    time = 0
    while time < (N - 1) // 2:
        time += 1

        for i in range(R):
            for j in range(C):
                s.add((i, j))

        while bombs:
            r, c = bombs.pop()
            s.discard((r, c))
            s.discard((r - 1, c))
            s.discard((r + 1, c))
            s.discard((r, c - 1))
            s.discard((r, c + 1))
        bombs = list(s)[:]
    while bombs:
        r, c = bombs.pop()
        answer[r][c] = 'O'
    for a in answer:
        print("".join(a))
