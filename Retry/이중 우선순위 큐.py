# Problem:
# Reference: https://www.acmicpc.net/problem/7662

# My Solution:
import heapq
import sys
from collections import defaultdict

for _ in range(int(sys.stdin.readline().rstrip())):
    min_heap = []
    max_heap = []
    nums = defaultdict(int)
    for __ in range(int(sys.stdin.readline().rstrip())):
        c, i = sys.stdin.readline().split()
        i = int(i)
        if c == 'I':
            heapq.heappush(min_heap, i)
            heapq.heappush(max_heap, (-i, i))
            nums[i] += 1
        elif c == 'D':
            if min_heap and max_heap:
                flag = False
                if i == 1:
                    pop = heapq.heappop(max_heap)
                    while nums[pop[1]] == 0:
                        if not max_heap:
                            flag = True
                            break
                        pop = heapq.heappop(max_heap)
                    if not flag:
                        nums[pop[1]] -= 1
                elif i == -1:
                    pop = heapq.heappop(min_heap)
                    while nums[pop] == 0:
                        if not min_heap:
                            flag = True
                            break
                        pop = heapq.heappop(min_heap)
                    if not flag:
                        nums[pop] -= 1

    flag = False
    if not max_heap:
        print("EMPTY")
        continue
    else:
        pop = heapq.heappop(max_heap)
        while nums[pop[1]] == 0:
            if not max_heap:
                print("EMPTY")
                flag = True
                break
            pop = heapq.heappop(max_heap)
        if not flag:
            print(pop[1], end=" ")

    if flag:
        continue
    else:
        pop = heapq.heappop(min_heap)
        while nums[pop] == 0:
            pop = heapq.heappop(min_heap)
        print(pop)
