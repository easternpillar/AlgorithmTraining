# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

# My Solution:
answer = []
for i in range(10):
    N, password = input().split()
    idx = 0
    while idx < len(password) - 1:
        if password[idx] == password[idx + 1]:
            password = password[:idx] + password[idx + 2:]
            idx -= 1
            if idx < 0:
                idx = 0
        else:
            idx += 1
    answer.append(password)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
