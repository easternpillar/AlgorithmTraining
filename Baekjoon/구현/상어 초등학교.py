# Problem:
# Reference: https://www.acmicpc.net/problem/21608

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
favors = [[] for _ in range(N * N + 1)]
classroom = [[-1 for _ in range(N)] for _ in range(N)]
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

for _ in range(N * N):
    temp = list(map(int, sys.stdin.readline().split()))
    student = temp[0]
    favors[student].extend(temp[1:])

    likes = -1
    empties = -1
    cand_pos = [0, 0]
    for i in range(N):
        for j in range(N):

            if classroom[i][j] == -1:
                tmp_likes = 0
                tmp_empties = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if N > nx >= 0 and N > ny >= 0:
                        if classroom[nx][ny] in favors[student]:
                            tmp_likes += 1
                        if classroom[nx][ny] == -1:
                            tmp_empties += 1

                if tmp_likes > likes or (tmp_likes == likes and tmp_empties > empties):
                    likes = tmp_likes
                    empties = tmp_empties
                    cand_pos[0] = i
                    cand_pos[1] = j

    classroom[cand_pos[0]][cand_pos[1]] = student

answer = 0
for i in range(N):
    for j in range(N):
        student = classroom[i][j]
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if N > nx >= 0 and N > ny >= 0:
                if classroom[nx][ny] in favors[student]:
                    cnt += 1
        if cnt > 0:
            answer += int(10 ** (cnt - 1))

print(answer)
