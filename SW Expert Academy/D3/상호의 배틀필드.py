# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LyE7KD2ADFAXc&categoryId=AV5LyE7KD2ADFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7

# My Solution:
def tank(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == '^':
                return [i, j], 'U'
            elif field[i][j] == 'v':
                return [i, j], 'D'
            elif field[i][j] == '<':
                return [i, j], 'L'
            elif field[i][j] == '>':
                return [i, j], 'R'


def command(field, comm):
    for c in comm:
        position, direction = tank(field)
        if c == 'U':
            direction = 'U'
            field[position[0]][position[1]] = '^'
            if position[0] - 1 >= 0:
                if field[position[0] - 1][position[1]] == '.':
                    field[position[0]][position[1]] = '.'
                    field[position[0] - 1][position[1]] = '^'
        elif c == 'D':
            direction = 'D'
            field[position[0]][position[1]] = 'v'
            if position[0] + 1 <= len(field) - 1:
                if field[position[0] + 1][position[1]] == '.':
                    field[position[0]][position[1]] = '.'
                    field[position[0] + 1][position[1]] = 'v'
        elif c == 'L':
            direction = 'L'
            field[position[0]][position[1]] = '<'
            if position[1] - 1 >= 0:
                if field[position[0]][position[1] - 1] == '.':
                    field[position[0]][position[1]] = '.'
                    field[position[0]][position[1] - 1] = '<'

        elif c == 'R':
            direction = 'R'
            field[position[0]][position[1]] = '>'
            if position[1] + 1 <= len(field[0]) - 1:
                if field[position[0]][position[1] + 1] == '.':
                    field[position[0]][position[1]] = '.'
                    field[position[0]][position[1] + 1] = '>'

        elif c == 'S':
            if direction == 'U':
                for i in range(position[0] - 1, -1, -1):
                    if field[i][position[1]] == '*':
                        field[i][position[1]] = '.'
                        break
                    elif field[i][position[1]] == '#':
                        break
            elif direction == 'D':
                for i in range(position[0] + 1, len(field), 1):
                    if field[i][position[1]] == '*':
                        field[i][position[1]] = '.'
                        break
                    elif field[i][position[1]] == '#':
                        break
            elif direction == 'L':
                for i in range(position[1] - 1, -1, -1):
                    if field[position[0]][i] == '*':
                        field[position[0]][i] = '.'
                        break
                    elif field[position[0]][i] == '#':
                        break
            else:
                for i in range(position[1] + 1, len(field[0]), 1):
                    if field[position[0]][i] == '*':
                        field[position[0]][i] = '.'
                        break
                    elif field[position[0]][i] == '#':
                        break
        print(c)
        for f in field:
            print(f)
    return field


answer = []
for i in range(int(input())):
    H, W = map(int, input().split())
    field = []
    for j in range(H):
        field.append(list(input()))
    N = int(input())
    answer.append(command(field, list(input())))

for i in range(len(answer)):
    print("#{}".format(i + 1), end=" ")
    for temp in answer[i]:
        print("".join(temp))
