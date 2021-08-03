# Problem:
# Reference: https://www.acmicpc.net/problem/2056

# My Solution:
import heapq
import sys
from collections import defaultdict


def topology():
    answer = 0
    hq = []
    for i in range(1, N + 1):
        if indegrees[i] == 0:
            heapq.heappush(hq, (times[i], i, answer))

    while hq:
        time, num, s_time = heapq.heappop(hq)
        # print(num, "번 작업 완료 시간:", s_time + time)
        answer = max(answer, s_time + time)

        for con in conn[num]:
            indegrees[con] -= 1
            if indegrees[con] == 0:
                heapq.heappush(hq, (times[con], con, answer))

    return answer


times = defaultdict(int)
N = int(sys.stdin.readline().rstrip())
indegrees = [0 for _ in range(N + 1)]
conn = [[] for _ in range(N + 1)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    times[i + 1] = temp[0]
    if temp[1] == 0:
        continue
    else:
        for j in range(2, len(temp), 1):
            conn[temp[j]].append(i + 1)
            indegrees[i + 1] += 1
print(topology())
