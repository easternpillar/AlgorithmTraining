# Problem:
# Given a board that is filled with values of cells, print the total values that the biggest rhombus has.

# My Solution:
answer = []

for i in range(int(input())):
    N = int(input())
    land = []
    tot = 0
    for j in range(N):
        land.append(list(map(int, list(input()))))
    for j in range(N // 2 + 1):
        tot += sum(land[j][N // 2 - j:N // 2 + j + 1])
    for j in range(N // 2 + 1, N):
        tot += sum(land[j][N // 2 - (N - j - 1):N // 2 + (N - j - 1) + 1])
    answer.append(tot)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
