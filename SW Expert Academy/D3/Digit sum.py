# Problem:
# Given a number, print the final number after digit sum.

# My Solution:
answer = []
for i in range(int(input())):
    num = str(sum(list(map(int, list(input())))))
    while int(num) >= 10:
        num = str(sum(list(map(int, list(num)))))
    answer.append(num)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
