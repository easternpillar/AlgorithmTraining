# Problem:
# Reference: https://www.acmicpc.net/problem/17144

# My Solution: DENIED.
# import sys
#
#
# def spread():
#     temp = [[0 for _ in range(C)] for _ in range(R)]
#
#     for i in range(R):
#         for j in range(C):
#             cnt = 0
#             if (i, j) in pos:
#                 continue
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in pos:
#                     temp[nx][ny] += A[i][j] // 5
#                     cnt += 1
#             A[i][j] -= (A[i][j] // 5) * cnt
#
#     for i in range(R):
#         for j in range(C):
#             A[i][j] += temp[i][j]
#
#
# def circulation():
#     cir1, cir2 = pos[0], pos[1]
#
#     row, col = cir1[0], cir1[1]
#     prev = -1
#     while col < C - 1:
#         col += 1
#         if prev == -1:
#             prev = A[row][col]
#             A[row][col] = 0
#         else:
#             A[row][col], prev = prev, A[row][col]
#
#     while row > 0:
#         row -= 1
#         if prev == -1:
#             prev = A[row][col]
#             A[row][col] = 0
#         else:
#             A[row][col], prev = prev, A[row][col]
#
#     while col > 0:
#         col -= 1
#         if prev == -1:
#             prev = A[row][col]
#             A[row][col] = 0
#         else:
#             A[row][col], prev = prev, A[row][col]
#
#     while row < cir1[0] - 1:
#         row += 1
#         if prev == -1:
#             prev = A[row][col]
#             A[row][col] = 0
#         else:
#             A[row][col], prev = prev, A[row][col]
#     A[cir1[0]][cir1[1]] = -1
#
#     row, col = cir2[0], cir2[1]
#     prev = -1
#     while col < C - 1:
#         col += 1
#         if prev == -1:
#             prev = A[row][col]
#             A[row][col] = 0
#         else:
#             A[row][col], prev = prev, A[row][col]
#
#     while row < R - 1:
#         row += 1
#         if prev == -1:
#             prev = A[row][col]
#             A[row][col] = 0
#         else:
#             A[row][col], prev = prev, A[row][col]
#
#     while col > 0:
#         col -= 1
#         if prev == -1:
#             prev = A[row][col]
#             A[row][col] = 0
#         else:
#             A[row][col], prev = prev, A[row][col]
#
#     while row > cir2[0] - 1:
#         row -= 1
#         if prev == -1:
#             prev = A[row][col]
#             A[row][col] = 0
#         else:
#             A[row][col], prev = prev, A[row][col]
#
#     A[cir1[0]][cir1[1]] = -1
#     A[cir2[0]][cir2[1]] = -1
#
#
# dx = (0, 1, 0, -1)
# dy = (1, 0, -1, 0)
#
# R, C, T = map(int, sys.stdin.readline().split())
# A = []
# for _ in range(R):
#     A.append(list(map(int, sys.stdin.readline().split())))
#
# pos = []
# for idx in range(R):
#     if A[idx][0] == -1:
#         pos.append((idx, 0))
#
# time = 0
# while time < T:
#     spread()
#     circulation()
#     time += 1
#
# answer = 0
# for a in A:
#     answer += sum(a)
#
# print(answer + 2)

def air_position():
    for i in range(R):
        if arr[i][0] == -1:
            return [i, 0], [i + 1, 0]


def dust_move():
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:
                val = 0

                if i - 1 >= 0 and arr[i - 1][j] != -1:
                    temp[i - 1][j] += arr[i][j] // 5
                    val += arr[i][j] // 5

                if i + 1 < R and arr[i + 1][j] != -1:
                    temp[i + 1][j] += arr[i][j] // 5
                    val += arr[i][j] // 5

                if j - 1 >= 0 and arr[i][j - 1] != -1:
                    temp[i][j - 1] += arr[i][j] // 5
                    val += arr[i][j] // 5

                if j + 1 < C and arr[i][j + 1] != -1:
                    temp[i][j + 1] += arr[i][j] // 5
                    val += arr[i][j] // 5
                temp[i][j] -= val
    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]


def air_move():
    temp = arr[up[0]][C - 1]
    for i in range(C - 1, 1, - 1):
        arr[up[0]][i] = arr[up[0]][i - 1]
    arr[up[0]][1] = 0

    temp_1 = arr[0][C - 1]
    for i in range(up[0] - 1):
        arr[i][C - 1] = arr[i + 1][C - 1]
    arr[up[0] - 1][C - 1] = temp

    temp_2 = arr[0][0]
    for i in range(C - 2):
        arr[0][i] = arr[0][i + 1]
    arr[0][C - 2] = temp_1

    for i in range(up[0] - 1, 1, -1):
        arr[i][0] = arr[i - 1][0]
    arr[1][0] = temp_2

    temp = arr[down[0]][C - 1]
    for i in range(C - 1, 1, -1):
        arr[down[0]][i] = arr[down[0]][i - 1]
    arr[down[0]][1] = 0

    temp_1 = arr[R - 1][C - 1]
    for i in range(R - 1, down[0] + 1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    arr[down[0] + 1][C - 1] = temp

    temp_2 = arr[R - 1][0]
    for i in range(C - 2):
        arr[R - 1][i] = arr[R - 1][i + 1]
    arr[R - 1][C - 2] = temp_1

    for i in range(down[0] + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    arr[R - 2][0] = temp_2


if __name__ == "__main__":

    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]

    up, down = air_position()

    for i in range(T):
        dust_move()
        air_move()

    total = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                total += arr[i][j]
    print(total)
