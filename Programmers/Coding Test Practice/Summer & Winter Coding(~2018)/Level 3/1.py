# Problem:
# Given a 5x5 board and a command sequence using 4 directions, return the number of paths that it passed.

# My Solution:
def solution(dirs):
    answer = 0
    updown = [[0 for _ in range(11)] for _ in range(10)]
    leftright = [[0 for _ in range(10)] for _ in range(11)]
    x = 5
    y = 5

    for d in dirs:
        if d == 'U':

            if x - 1 >= 0:
                x -= 1
                if updown[x][y] == 1:

                    continue
                else:
                    answer += 1
                    updown[x][y] = 1
        elif d == 'D':

            if x + 1 <= 10:
                x += 1
                if updown[x - 1][y] == 1:

                    continue
                else:
                    answer += 1
                    updown[x - 1][y] = 1
        elif d == 'L':

            if y - 1 >= 0:
                y -= 1
                if leftright[x][y] == 1:

                    continue
                else:
                    answer += 1
                    leftright[x][y] = 1
        else:

            if y + 1 <= 10:
                y += 1
                if leftright[x][y - 1] == 1:

                    continue
                else:
                    answer += 1
                    leftright[x][y - 1] = 1

    return answer
