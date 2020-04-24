# Problem:
# Given 4 cog wheels, the number of cog wheel, and the direction of rotation, return the total score after K rotations.
# Conditions(s):
# 1. If the cog is in contact with the same pole, it will not rotate, else it will rotate in the opposite direction.
# 1. If the 12 o'clock direction of the first cogwheel is the S pole, you get one point.
# 2. If the 12 o'clock direction of the second cog is the S pole, you get two points.
# 3. If the 12 o'clock direction of the third cogwheel is the S pole, you get four points.
# 4. If the 12 o'clock direction of the fourth gear is the S pole, you get eight points.

# My Solution:
from collections import deque


def rightcog(cog, face, index, direction):
    d = direction
    for i in range(index + 1, 4, 1):
        if face[i - 1][0] == face[i][1]:
            break
        else:
            if d == 1:
                cog[i].append(cog[i].popleft())
            else:
                cog[i].appendleft(cog[i].pop())
            d *= -1


def leftcog(cog, face, index, direction):
    d = direction
    for i in range(index - 1, -1, -1):
        if face[i + 1][1] == face[i][0]:
            break
        else:
            if d == 1:
                cog[i].append(cog[i].popleft())
            else:
                cog[i].appendleft(cog[i].pop())
            d *= -1


cogs = [deque(list(map(int, list(input().strip())))) for i in range(4)]
n = int(input())
com = deque([list(map(int, list(input().split()))) for j in range(n)])
faced = [[cogs[i][2], cogs[i][6]] for i in range(4)]

while com:
    c = com.popleft()
    rightcog(cogs, faced, c[0] - 1, c[1])
    leftcog(cogs, faced, c[0] - 1, c[1])

    if c[1] == 1:
        cogs[c[0] - 1].appendleft(cogs[c[0] - 1].pop())

    else:
        cogs[c[0] - 1].append(cogs[c[0] - 1].popleft())
    faced = [[cogs[i][2], cogs[i][6]] for i in range(4)]

tot = 0
for i in range(4):
    if cogs[i][0] == 1:
        tot += cogs[i][0] * (2 ** i)

print(tot)