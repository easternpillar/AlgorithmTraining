# Problem:
# Reference: https://www.acmicpc.net/problem/16235

# My Solution: Denied.
# import heapq
#
# n, m, k = map(int, input().split())
# add = [list(map(int, input().split())) for i in range(n)]
# ground = [[5 for i in range(n)] for j in range(n)]
# trees = [[[] for i in range(n)] for j in range(n)]
#
# for i in range(m):
#     x, y, a = map(int, input().split())
#     heapq.heappush(trees[x - 1][y - 1], a)
#
# year = 0
# answer = 0
# dir = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
#
# while year < k:
#     # 봄, 여름
#     fives = []
#     for i in range(n):
#         for j in range(n):
#             alive = []
#             dead = 0
#             while trees[i][j]:
#                 age = heapq.heappop(trees[i][j])
#                 if ground[i][j] >= age:
#                     ground[i][j] -= age
#                     alive.append(age + 1)
#                     if (age + 1) % 5 == 0:
#                         fives.append([i, j])
#                 else:
#                     dead += age // 2
#             while alive:
#                 heapq.heappush(trees[i][j], alive.pop())
#             ground[i][j] += dead
#
#     # 가을
#     while fives:
#         xpos, ypos = fives.pop()
#         for dx, dy in dir:
#             nx = xpos + dx
#             ny = ypos + dy
#             if 0 <= nx <= n-1 and 0 <= ny <= n-1:
#                 heapq.heappush(trees[nx][ny], 1)
#
#     # 겨울
#     for i in range(n):
#         for j in range(n):
#             ground[i][j] += add[i][j]
#
#     year += 1
#
# for i in range(n):
#     for j in range(n):
#         answer += len(trees[i][j])
#
# print(answer)

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

ground = [[5] * N for _ in range(N)]

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if len(tree[i][j]) <= 0: continue
            tree[i][j].sort()
            idx = 0
            while idx < len(tree[i][j]):
                if tree[i][j][idx] <= ground[i][j]:
                    ground[i][j] -= tree[i][j][idx]
                    tree[i][j][idx] += 1
                    idx += 1
                else:
                    die = tree[i][j][idx:]
                    for now in die:  # 죽은나무!
                        ground[i][j] += (now // 2)
                    tree[i][j] = tree[i][j][:idx]
                    break

    di = [[-1, 0], [0, -1], [1, 0], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    for i in range(N):
        for j in range(N):
            c = 0
            if tree[i][j]:
                for now in tree[i][j]:
                    if now % 5 == 0:
                        c += 1
            if c > 0:
                for k in range(8):
                    ni = i + di[k][0]
                    nj = j + di[k][1]
                    if 0 <= ni < N and 0 <= nj < N:
                        for _ in range(c):
                            tree[ni][nj].append(1)

    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)
