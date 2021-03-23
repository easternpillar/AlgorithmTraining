# Problem:
# Given a sequence of integers, print the minimum integer that cannot be made.

# My Solution:
for i in range(int(input())):
    N = int(input())
    temp = ""
    while True:
        temp += "".join(input().split())
        if len(temp) == N:
            break

    check = 0
    while True:
        if str(check) not in temp:
            print("#{} {}".format(i + 1, check))
            break
        check += 1