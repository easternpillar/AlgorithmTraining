# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGEbd6cjMDFAUo&categoryId=AWXGEbd6cjMDFAUo&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9

# My Solution:
answer = []
for i in range(int(input())):
    N = int(input())
    dummies = [int(input()) for _ in range(N)]
    dummies.sort()
    avg = sum(dummies) // N
    tot = 0

    for d in dummies:
        if d >= avg:
            break
        tot += avg - d
    answer.append(tot)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
