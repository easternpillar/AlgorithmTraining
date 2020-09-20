# Problem:
# Given NxN aisle and the positions of teachers and students, return if all students can get out of surveillance when 3 obstacles are installed.
# Condition(s):
# 1. Teachers watch up, down, left and right.
# 2. Teachers cannot watch over obstacles.

# My Solution:
import sys
from collections import deque
from itertools import combinations

N = int(sys.stdin.readline())
aisle = []
empty = []
teacher = []

for i in range(N):
    temp = list(sys.stdin.readline().rstrip().split())
    for j in range(N):
        if temp[j] == 'X':
            empty.append([i, j])
        elif temp[j] == 'T':
            teacher.append([i, j])
    aisle.append(temp)

flag1=False
for comb in list(combinations(empty, 3)):
    # print(comb)
    flag = True
    for x, y in teacher:
        # print("선생",x,y)
        nx = x
        ny = y
        # print("위 검사")
        while nx - 1 >= 0:
            nx -= 1
            # print(nx,ny)
            if [nx, ny] in comb:
                # print("장애물",nx,ny,comb)
                break
            elif aisle[nx][ny] == 'S':
                # print("학생 발견")
                flag = False
                break

        nx = x
        ny = y
        # print("아래 검사")
        while nx + 1 < N:
            nx += 1
            # print(nx,ny)
            if [nx, ny] in comb:
                # print("장애물",nx,ny,comb)
                break
            elif aisle[nx][ny] == 'S':
                # print("학생 발견")
                flag = False
                break

        nx = x
        ny = y
        # print("왼쪽 검사")
        while ny - 1 >= 0:
            ny -= 1
            # print(nx,ny)
            if [nx, ny] in comb:
                # print("장애물", nx, ny, comb)
                break
            elif aisle[nx][ny] == 'S':
                # print("학생 발견")
                flag = False
                break

        nx = x
        ny = y
        # print("오른쪽 검사")
        while ny + 1 < N:
            ny += 1
            # print(nx,ny)
            if [nx, ny] in comb:
                # print("장애물", nx, ny, comb)
                break
            elif aisle[nx][ny] == 'S':
                # print("학생 발견")
                flag = False
                break

    if flag:
        # print("성공:",comb)
        flag1 = True
        break

if flag1:
    print("YES")
else:
    print("NO")
