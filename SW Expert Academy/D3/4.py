# Problem:
# Given the order of pressing the buttons of robot o and robot b, print the minimum required time.
# Condition(s):
# 1. The initial positions of robots are 1.
# 2. It takes 1 time to move one space or press a button.
# 3. The robots can not press the button at the same time.

# My Solution:
from collections import deque

TC = int(input())
for i in range(TC):
    tasks = input().split()[1:]
    tasks = list(zip([tasks[i] for i in range(0, len(tasks), 2)], [int(tasks[j]) for j in range(1, len(tasks), 2)]))

    q = deque(tasks)
    b_des = deque([])
    o_des = deque([])

    for t in tasks:
        if t[0] == 'B':
            b_des.append(t[1])
        else:
            o_des.append(t[1])

    b_pos = 1
    o_pos = 1
    time = 0
    while q:
        robot, des = q.popleft()

        if robot == 'B':
            time += abs(des - b_pos) + 1

            if o_des:
                if abs(des-b_pos)+1 >= abs(o_pos - o_des[0]):
                    o_pos = o_des[0]
                else:
                    o_pos += (abs(des-b_pos)+1) * ((o_des[0] - o_pos) // abs(o_des[0] - o_pos))

            b_pos = des

            if len(b_des) > 1:
                b_des.popleft()
        else:
            time += abs(des - o_pos) + 1

            if b_des:
                if abs(des-o_pos)+1 >= abs(b_pos - b_des[0]):
                    b_pos = b_des[0]
                else:
                    b_pos += (abs(des-o_pos)+1) * ((b_des[0] - b_pos) // abs(b_des[0] - b_pos))

            o_pos = des

            if len(o_des) > 1:
                o_des.popleft()

    print("#{} {}".format(i + 1, time))
