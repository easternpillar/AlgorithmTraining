# Problem:
#

# My Solution:
# 기능
# 1. 추천: 난이도 -> 문제 번호
# 2. 추가: 번호와 난이도 조합
# 3. 제거: 번호로 조회 후 제거

# 고려사항
# 1. 문제 저장 자료구조: 이중 정렬 -> 이중 우선순위 큐
# 2. 제거 탐색 알고리즘: 제거할 문제번호 위치 탐색
import sys
import heapq
from collections import defaultdict

max_heap = []
min_heap = []
cache = defaultdict(bool)
for _ in range(int(sys.stdin.readline().rstrip())):
    P, L = map(int, sys.stdin.readline().split())
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L, P))
    cache[P] = False

for _ in range(int(sys.stdin.readline().rstrip())):
    command = sys.stdin.readline().split()
    if command[0] == 'recommend':
        answer=-1
        if command[1] == '1':
            answer = heapq.heappop(max_heap)
            while cache[-answer[1]]:
                answer = heapq.heappop(max_heap)
            print(-answer[1])
            heapq.heappush(max_heap, answer)
        elif command[1] == '-1':
            answer = heapq.heappop(min_heap)
            while cache[answer[1]]:
                answer = heapq.heappop(min_heap)
            print(answer[1])
            heapq.heappush(min_heap, answer)
    elif command[0] == 'add':
        heapq.heappush(max_heap, (-int(command[2]), -int(command[1])))
        heapq.heappush(min_heap, (int(command[2]), int(command[1])))
        cache[int(command[1])] = False
    elif command[0] == 'solved':
        cache[int(command[1])] = True
    print(max_heap)
    print(min_heap)
    print(cache)
