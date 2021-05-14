# Problem:
# Given the structure of office, return the minimum number of blind spots.

# My Solution:
from collections import deque
import copy


def camera1(o, pos):
    re = []

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while r > 0:
        r -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while r < len(temp) - 1:
        r += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while c > 0:
        c -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while c < len(temp[0]) - 1:
        c += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    return re


def camera2(o, pos):
    temp = copy.deepcopy(o)
    re = []

    r, c = pos[0], pos[1]
    while r > 0:
        r -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while r < len(temp) - 1:
        r += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while c > 0:
        c -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c < len(temp[0]) - 1:
        c += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    return re


def camera3(o, pos):
    re = []

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while r > 0:
        r -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c < len(temp[0]) - 1:
        c += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while r < len(temp) - 1:
        r += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c < len(temp[0]) - 1:
        c += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while c > 0:
        c -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while r > 0:
        r -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while c > 0:
        c -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while r < len(temp) - 1:
        r += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    return re


def camera4(o, pos):
    re = []

    # 오른쪽, 위, 왼쪽
    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while r > 0:
        r -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c > 0:
        c -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c < len(temp[0]) - 1:
        c += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    # 오른쪽, 아래, 왼쪽
    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while r < len(temp) - 1:
        r += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c > 0:
        c -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c < len(temp[0]) - 1:
        c += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    # 왼쪽, 위, 아래
    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while c > 0:
        c -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while r < len(temp) - 1:
        r += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while r > 0:
        r -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    # 오른쪽, 위, 아래
    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while c < len(temp[0]) - 1:
        c += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while r > 0:
        r -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while r < len(temp) - 1:
        r += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue
    re.append(temp)

    return re


def camera5(o, pos):
    temp = copy.deepcopy(o)
    r, c = pos[0], pos[1]
    while r > 0:
        r -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c > 0:
        c -= 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while c < len(temp[0]) - 1:
        c += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    r, c = pos[0], pos[1]
    while r < len(temp) - 1:
        r += 1
        if temp[r][c] == 6:
            break
        if temp[r][c] == 0:
            temp[r][c] = '#'
        else:
            continue

    return temp


r, c = map(int, input().split())
office = [list(map(int, list(input().split()))) for _ in range(r)]

origin=0
for i in range(len(office)):
    for j in range(len(office[i])):
        if office[i][j]==0:
            origin+=1

offices = deque([office])

cam = deque()
for i in range(r):
    for j in range(c):
        if 1 <= office[i][j] <= 5:
            cam.append([i, j])

answer=set()
while cam:
    c = cam.popleft()
    x, y = c[0], c[1]
    new_office = []

    while offices:
        o = offices.popleft()

        if o[x][y] == 1:
            new_office.extend(camera1(o, [x, y]))
        elif o[x][y] == 2:
            new_office.extend(camera2(o, [x, y]))
        elif o[x][y] == 3:
            new_office.extend(camera3(o, [x, y]))
        elif o[x][y] == 4:
            new_office.extend(camera4(o, [x, y]))
        else:
            new_office.append(camera5(o, [x, y]))

    offices.extend(new_office)

    if not cam:
        while offices:
            temp=offices.popleft()
            cnt=0
            for i in range(len(temp)):
                for j in range(len(temp[i])):
                    if temp[i][j]==0:
                        cnt+=1

            answer.add(cnt)
        break

if answer:
    print(min(answer))
else:
    print(origin)