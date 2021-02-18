# Problem:
# Given an NxN board with Go stones, print out whether there are 5 or more Go stones in a row.

# My Solution:
global board


def horizontal(x, y):
    global board
    cnt = 1
    tx, ty = x, y
    while ty > 0:
        ty -= 1
        if board[tx][ty] == 'o':
            cnt += 1
        else:
            break

    tx, ty = x, y
    while ty < len(board) - 1:
        ty += 1
        if board[tx][ty] == 'o':
            cnt += 1
        else:
            break

    if cnt >= 5:
        return True
    else:
        return False


def vertical(x, y):
    global board
    cnt = 1
    tx, ty = x, y
    while tx > 0:
        tx -= 1
        if board[tx][ty] == 'o':
            cnt += 1
        else:
            break

    tx, ty = x, y
    while tx < len(board) - 1:
        tx += 1
        if board[tx][ty] == 'o':
            cnt += 1
        else:
            break

    if cnt >= 5:
        return True
    else:
        return False


def diagonal(x, y):
    global board
    cnt = 1
    tx, ty = x, y
    while tx > 0 and ty > 0:
        tx -= 1
        ty -= 1
        if board[tx][ty] == 'o':
            cnt += 1
        else:
            break

    tx, ty = x, y
    while tx < len(board) - 1 and ty < len(board) - 1:
        tx += 1
        ty += 1
        if board[tx][ty] == 'o':
            cnt += 1
        else:
            break

    if cnt >= 5:
        return True
    else:
        cnt = 1
        tx, ty = x, y
        while tx > 0 and ty < len(board) - 1:
            tx -= 1
            ty += 1
            if board[tx][ty] == 'o':
                cnt += 1
            else:
                break

        tx, ty = x, y
        while tx < len(board) - 1 and ty > 0:
            tx += 1
            ty -= 1
            if board[tx][ty] == 'o':
                cnt += 1
            else:
                break

        if cnt >= 5:
            return True
        else:
            return False


T = int(input())
for i in range(T):
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(input()))

    print("#{}".format(i + 1), end=' ')
    boolean = False
    for j in range(N):
        for k in range(N):
            if board[j][k] == 'o':
                if horizontal(j, k) or vertical(j, k) or diagonal(j, k):
                    boolean = True
                    break
        if boolean:
            break
    if boolean:
        print("YES")
    else:
        print('NO')
