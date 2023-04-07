# Reference: https://www.acmicpc.net/problem/19237


N, M, k = map(int, input().split())
shark_pos = [0 for _ in range(M + 1)]
smell = [[0 for _ in range(N)] for _ in range(N)]
prior = [0]

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] != 0:
            shark_pos[temp[j]] = [i, j]

shark_dir = [0]
shark_dir.extend(list(map(int, input().split())))

for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    prior.append(temp)
time = 0
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

while True:
    time += 1
    # 1. 자기 위치 냄새 뿌리기
    for i in range(1, M + 1):
        if shark_pos[i] != 0:
            x, y = shark_pos[i]
            smell[x][y] = [i, k]

    # 2. 상어 이동: 우선순위 순으로 이동 + 냄새 없는 곳 -> 없으면 자기 냄새 + 이동방향 업데이트
    for i in range(1, M + 1):
        if shark_pos[i] != 0:
            x, y = shark_pos[i]
            flag = False
            for direction in prior[i][shark_dir[i] - 1]:
                nx = x + dx[direction]
                ny = y + dy[direction]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if smell[nx][ny] != 0 and smell[nx][ny][0] != i:
                    continue
                elif smell[nx][ny] == 0:
                    shark_dir[i] = direction
                    shark_pos[i] = [nx, ny]
                    flag = True
                    break
            if not flag:
                for direction in prior[i][shark_dir[i] - 1]:
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if smell[nx][ny][0] == i:
                        shark_dir[i] = direction
                        shark_pos[i] = [nx, ny]
                        break
    # 3. 상어 위치 확인해서 겹치는 경우 낮은 숫자 제외 모두 제거
    for i in range(1, M):
        main = shark_pos[i]
        for j in range(i + 1, M + 1):
            if shark_pos[j] == main:
                shark_pos[j] = 0
    # 4. 냄새 1씩 제거
    for i in range(N):
        for j in range(N):
            if smell[i][j] != 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = 0
    # 5. 1번 상어만 남은 경우 break
    flag = True
    for i in range(1, M + 1):
        if i != 1 and shark_pos[i] != 0:
            flag = False
            break
    if flag:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break
