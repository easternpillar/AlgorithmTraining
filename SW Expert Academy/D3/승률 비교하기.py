# Problem:
# Given the totals of alice and bob, print the winners.

# My Solution:
answer = []
for i in range(int(input())):
    A, B, C, D = map(int, input().split())
    a = A / B
    b = C / D

    if a == b:
        answer.append("DRAW")
    elif a > b:
        answer.append("ALICE")
    else:
        answer.append("BOB")

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
