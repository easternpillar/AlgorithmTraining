# Problem:
# Given the size of the wall, tasks that install or delete the columns and beams in order, return the state of the structure.
# Condition(s):
# 1. The column must be on the floor, on one end of the beam, or on another.
# 2. Either end of the beam must be on top of the column, or both ends must be connected simultaneously with the other beam.

# My Solution:
def check(ans):
    for x, y, what in ans:
        if what == 0:
            if y == 0 or [x - 1, y, 1] in ans or [x, y, 1] in ans or [x, y - 1, 0] in ans:
                continue
            else:
                return False

        elif what == 1:
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans or ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for f in build_frame:
        x, y, what, how = f

        if how == 1:
            answer.append([x, y, what])
            if check(answer) is False:
                answer.remove([x, y, what])
        else:
            answer.remove([x, y, what])
            if check(answer) is False:
                answer.append([x, y, what])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer
