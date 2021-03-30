# Problem:
# Given the commands of max heap, print the output.
# Condition(s):
# 1. 1 means push.
# 2. 2 means pop.

# My Solution:
import heapq

answer = []
for i in range(int(input())):
    N = int(input())
    comm = []
    heap = []
    out = []
    for j in range(N):
        comm.append(tuple(map(int, input().split())))

    for c in comm:
        if c[0] == 2:
            if not heap:
                out.append(1)
            else:
                out.append(heapq.heappop(heap))
        else:
            heapq.heappush(heap, -c[1])

    answer.append(out)

for i in range(len(answer)):
    print("#{}".format(i + 1), end=' ')
    for j in range(len(answer[i])):
        print(-answer[i][j], end=' ')
    print()
