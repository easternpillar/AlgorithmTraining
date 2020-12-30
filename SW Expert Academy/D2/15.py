# Problem:
# Given a two-dimensional array, print the array rotated by 90, 180 and 270 degrees.

# My Solution:
T = int(input())
for i in range(T):
    print("#{}".format(i + 1))
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(str, input().split())))

    r3 = list(reversed(list(map(list, zip(*board)))))
    r2 = list(reversed(list(map(list, zip(*r3)))))
    r1 = list(reversed(list(map(list, zip(*r2)))))

    for k in range(N):
        print("".join(r1[k]), end=" ")
        print("".join(r2[k]), end=" ")
        print("".join(r3[k]))
