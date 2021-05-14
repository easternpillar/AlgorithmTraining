# Problem:
# Given a case of Dummy game, return the time that the game is over.

# My Solution:
from collections import deque

size = int(input())

n_apple = int(input())
pos_apple=[]
for _ in range(n_apple):
    pos_apple.append(list(map(int, input().split())))

n_dir = int(input())
dir_li = []
for i in range(n_dir):
    dir_li.append(list(input().split()))
    dir_li[i][0] = int(dir_li[i][0])
q = deque(dir_li)

cur_dir = 'R'
head = [1, 1]
length = 1
tail = []
q_tail=deque(tail)
time = 0

while True:
    if head[0] > size or head[1] > size or head[0]<1 or head[1]<1:
        break

    if q:
        temp = q.popleft()

        while time < temp[0]:
            if head[0] > size or head[1] > size or head[0]<1 or head[1]<1:
                break

            q_tail.append([head[0], head[1]])
            time += 1

            if cur_dir == 'R':
                head[1] += 1
            elif cur_dir == 'L':
                head[1] -= 1
            elif cur_dir == 'U':
                head[0] -= 1
            else:
                head[0] += 1

            if head in q_tail:
                break

            while len(q_tail) > length-1:
                q_tail.popleft()

            if [head[0], head[1]] in pos_apple:
                pos_apple.remove([head[0],head[1]])
                length += 1

        if time==temp[0]:
            if temp[1]=='D':
                if cur_dir=='U':
                    cur_dir='R'
                elif cur_dir=='D':
                    cur_dir='L'
                elif cur_dir=='L':
                    cur_dir='U'
                else:
                    cur_dir='D'
            else:
                if cur_dir=='U':
                    cur_dir='L'
                elif cur_dir=='D':
                    cur_dir='R'
                elif cur_dir=='L':
                    cur_dir='D'
                else:
                    cur_dir='U'

    else:
        q_tail.append([head[0], head[1]])
        time += 1

        if cur_dir == 'R':
            head[1] += 1
        elif cur_dir == 'L':
            head[1] -= 1
        elif cur_dir == 'U':
            head[0] -= 1
        else:
            head[0] += 1

        if head in q_tail:
            break

        while len(q_tail) > length - 1:
            q_tail.popleft()

        if [head[0], head[1]] in pos_apple:
            pos_apple.remove([head[0], head[1]])
            length += 1

    if head in q_tail:
        break

print(time)
