# Problem:
# Given the populations of nations, return the number of moves.
# Condition(s):
# 1. If the population gap between the two countries sharing the border is more than L and less than R, the two countries will open the shared border today.
# 2. If all the borders that must be opened under the above conditions are open, the population shift begins.
# 3. If the border is open and you can travel by the adjacent Khan Bay, the country is called the Union for the day.
# 4. The population of each compartment in the union is (the population of the union) / (the number of compounded compartments). Throw away the decimal point for convenience.
# 5. Dismantle the Union, close all borders.

# My Solution:
from collections import deque

n, l, r = map(int, input().split())

nations = []
for _ in range(n):
    nations.append(list(map(int, input().split())))

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0

while True:
    flag = 0
    tot_visited = set()

    for x, y in ([i, j] for i in range(n) for j in range(n)):
        if (x, y) in tot_visited:
            continue
        q = deque([[x, y]])

        tot = nations[x][y]
        cnt = 1
        visited = set()
        while q:
            pop = q.popleft()

            if (pop[0], pop[1]) in tot_visited:
                continue

            for dx, dy in dir:
                nx = pop[0] + dx
                ny = pop[1] + dy

                if nx >= n or nx < 0 or ny >= n or ny < 0 or (nx, ny) in visited or (nx, ny) in tot_visited:
                    continue

                if l <= abs(nations[nx][ny] - nations[pop[0]][pop[1]]) <= r:
                    visited.update([(pop[0], pop[1]), (nx, ny)])
                    q.append([nx, ny])
                    tot += nations[nx][ny]
                    flag = 1
                    cnt += 1

        tot_visited.update(visited)
        avg = tot // cnt
        for x, y in visited:
            nations[x][y] = avg

    if flag == 0:
        break
    else:
        answer += 1

print(answer)
