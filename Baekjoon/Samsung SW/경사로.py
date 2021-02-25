# Problem:
# Given the heights of NxN routes and L length ramps, return the number of available routes.
# Condition(s):
# 1. Only the routes with the same heights can be passed.
# 2. Ramps can be set on L same height blocks.

# My Solution:
size, length = map(int, input().split())
routes = [list(map(int, list(input().split()))) for i in range(size)]

answer = 0
for _ in range(2):

    for i in range(size):
        value = routes[i][0]
        bcnt = 0

        j = 0
        while j < size:
            if routes[i][j] == value:
                bcnt += 1

            elif routes[i][j] - value == 1:
                if bcnt >= length:
                    value = routes[i][j]
                    bcnt = 0
                    continue

                else:
                    answer -= 1
                    break

            elif value - routes[i][j] == 1:
                value = routes[i][j]
                scnt = 0

                for k in range(j, size, 1):
                    if k >= j + length:
                        break

                    if routes[i][k] == value:
                        scnt += 1

                    else:
                        break

                if scnt >= length:
                    j = j + length - 1
                    value = routes[i][j]
                    bcnt = -1
                    continue

                else:
                    answer -= 1
                    break

            else:
                answer -= 1
                break

            j += 1

        answer += 1

    routes = list(map(list, zip(*routes)))

print(answer)
