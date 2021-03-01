# Problem:
# Given the number of nodes and edges, print the number of triangles.

# My Solution:
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    conn = [[] for _ in range(N + 1)]
    answer = 0
    print("#{}".format(i + 1), end=" ")

    for j in range(M):
        x, y = map(int, input().split())
        if x < y:
            conn[x].append(y)
        else:
            conn[y].append(x)

    for j in range(N + 1):
        for k in conn[j]:
            for l in conn[k]:
                if l in conn[j]:
                    answer += 1

    print(answer)
