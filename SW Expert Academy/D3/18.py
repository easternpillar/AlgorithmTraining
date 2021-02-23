# Problem:
#

# My Solution:
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    conn = [[] for _ in range(N + 1)]
    for j in range(M):
        x, y = map(int, input())
        conn[x].append(y)
        conn[y].append(x)
