# Problem:
# Given two positive integers, print the sum of those.

# My Solution:
answer = []
for i in range(int(input())):
    A, B = map(int, input().split())
    answer.append(A + B)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
