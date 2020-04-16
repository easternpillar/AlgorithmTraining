# Problem:
# Given the number of examination rooms, student for each room, and the number of students that supervisor and vice-supervisor can supervise, return the minimum number of supervisors.
# Condition(s):
# 1. Chief supervisor should be one.
# 2. vice supervisor can be more than one.

# My Solution:
tn = int(input())
sn = list(map(int, list(input().split())))
vn = list(map(int, list(input().split())))

total = 0

for i in range(tn):
    if sn[i] > 0:
        total += 1
        sn[i] -= vn[0]
        if sn[i] > 0:
            total += sn[i] // vn[1]
            if sn[i] % vn[1] > 0:
                total += 1
    else:
        continue

print(total)
