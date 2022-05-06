# 링크: https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3
# 문제 접근
# 1. bfs
from collections import deque


def bfs(s, p):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque([(s[0], s[1], 0)])
    visited = []

    while q:
        x, y, distance = q.popleft()
        if distance >= 2:
            continue
        if distance == 0:
            visited.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 4 and 0 <= ny <= 4 and (nx, ny) not in visited:
                if p[nx][ny] == 'P':
                    print(x, y, nx, ny)
                    return 0
                elif p[nx][ny] == 'X':
                    continue
                else:
                    q.append((nx, ny, distance + 1))
    return 1


def solution(places):
    answer = []

    for place in places:
        li = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    li.append((i, j, 0))
        flag = 1
        for start in li:
            if bfs(start, place) == 0:
                flag = 0
        answer.append(flag)

    return answer