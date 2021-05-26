# Problem:
# Reference: https://www.acmicpc.net/problem/11286

# My Solution:
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
h = []
for _ in range(N):
    temp = int(sys.stdin.readline().rstrip())
    if temp == 0:
        if not h:
            print(0)
            continue

        same = []
        mini = heapq.heappop(h)
        same.append(mini)

        while h:
            pop = heapq.heappop(h)
            if pop[0] == mini[0]:
                same.append(pop)
                continue
            else:
                heapq.heappush(h, pop)
                break

        same.sort(key=lambda x: x[1], reverse=True)
        print(same.pop()[1])

        for s in same:
            heapq.heappush(h, s)

    else:
        heapq.heappush(h, (abs(temp), temp))
