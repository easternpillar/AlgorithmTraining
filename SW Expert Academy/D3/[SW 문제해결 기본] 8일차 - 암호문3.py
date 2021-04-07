# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14zIwqAHwCFAYD&categoryId=AV14zIwqAHwCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

# My Solution:
answer = []
for i in range(10):
    N = int(input())
    encrypted = input().split()
    N = int(input())
    command = input().split()
    idx = 0

    while idx < len(command):
        if command[idx] == 'I':
            x, y = int(command[idx + 1]), int(command[idx + 2])
            nums = command[idx + 3:idx + 3 + y]
            for j in range(y):
                encrypted.insert(x + j, nums[j])
        if command[idx] == 'D':
            x, y = int(command[idx + 1]), int(command[idx + 2])
            encrypted = encrypted[:x] + encrypted[x + y:]
        if command[idx] == 'A':
            y = int(command[idx + 1])
            nums = command[idx + 2:idx + 2 + y]
            encrypted.extend(nums)
        idx += 1
    answer.append(encrypted[:10])

for i in range(len(answer)):
    print("#{}".format(i + 1), end=" ")
    for j in range(len(answer[i])):
        print(answer[i][j], end=" ")
    print()
