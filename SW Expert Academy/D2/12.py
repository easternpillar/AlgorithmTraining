# Problem:
# Given a completed sudoku puzzle, print if it is correct.

# My Solution:
T = int(input())

for i in range(T):
    sudoku = []
    flag = 1
    print("#{}".format(i + 1), end=" ")
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    for line in sudoku:
        if len(set(line)) < 9:
            flag = 0
            break

    if flag == 1:
        for line in list(zip(*sudoku)):
            if len(set(line)) < 9:
                flag = 0
                break

    if flag == 1:
        for j in range(0, 9, 3):
            for k in range(0, 9, 3):
                temp = []
                for l in range(3):
                    for m in range(3):
                        temp.append(sudoku[j+l][k + m])
                if len(set(temp)) < 9:
                    flag = 0
                    break

    print(flag)
