# Problem:
# Given a mxn room with 0 if the space is not cleaned yet, 1 if it is wall, return the size of space to clean.
# Condition(s):
# 1. First, clean the current space.
# 2. From the current position, proceed one by one from the left in relation to the current direction.
# 3. If there is a space on the left side that has not yet been cleaned, rotate in that direction, then advance one space and proceed from number one.
# 4. If there is no room for cleaning in the left direction, rotate in that direction and return to number 2.
# 5. If all four directions have already been cleaned or are walls, move back one space and return to No. 2.
# 6. If all four directions are already cleaned or are walls, and the back direction is a wall and cannot be reversed, it stops working.

# My Solution:
r, c = map(int, input().split())
x, y, d = map(int, input().split())
pos = [x, y]

room = []
for i in range(r):
    room.append(list(map(int, list(input().split()))))

cnt = 0
answer = 1
while True:
    room[pos[0]][pos[1]] = 2

    if cnt == 4:
        if d == 0:
            if pos[0] + 1 > r - 1:
                break
            elif room[pos[0] + 1][pos[1]] == 1:
                break
            else:
                pos[0] += 1
                cnt = 0
        elif d == 1:
            if pos[1] - 1 < 0:
                break
            elif room[pos[0]][pos[1] - 1] == 1:
                break
            else:
                pos[1] -= 1
                cnt = 0
        elif d == 2:
            if pos[0] - 1 < 0:
                break
            elif room[pos[0] - 1][pos[1]] == 1:
                break
            else:
                pos[0] -= 1
                cnt = 0
        else:
            if pos[1] + 1 > c - 1:
                break
            elif room[pos[0]][pos[1] + 1] == 1:
                break
            else:
                pos[1] += 1
                cnt = 0
    if d == 0:
        d = 3
        if pos[1] - 1 >= 0:
            if room[pos[0]][pos[1] - 1] == 0:
                pos[1] -= 1
                cnt = 0
                answer += 1
            else:
                cnt += 1
    elif d == 1:
        d = 0
        if pos[0] - 1 >= 0:
            if room[pos[0] - 1][pos[1]] == 0:
                pos[0] -= 1
                cnt = 0
                answer += 1
            else:
                cnt += 1
    elif d == 2:
        d = 1
        if pos[1] + 1 >= 0:
            if room[pos[0]][pos[1] + 1] == 0:
                pos[1] += 1
                cnt = 0
                answer += 1
            else:
                cnt += 1
    else:
        d = 2
        if pos[0] + 1 >= 0:
            if room[pos[0] + 1][pos[1]] == 0:
                pos[0] += 1
                cnt = 0
                answer += 1
            else:
                cnt += 1

print(answer)
