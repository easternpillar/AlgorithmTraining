# Problem:
# Given the commands of acceleration, print the total distance traveled.
# Condition(s):
# 1. The initial speed is 0.
# 2. Command 0 means maintaining the current speed.
# 3. Command 1 means acceleration by the next number.
# 4. Command 2 means deceleration by the next number.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    distance = 0
    velocity = 0
    print("#{}".format(i + 1), end=" ")

    for j in range(N):
        c = list(map(int, input().split()))
        if len(c) > 1:
            flag, accel = c[0], c[1]
        else:
            flag = c[0]

        if flag == 0:
            distance += velocity
        elif flag == 1:
            velocity += accel
            distance += velocity
        else:
            velocity -= accel
            if velocity < 0:
                velocity = 0
            distance += velocity

    print(distance)
