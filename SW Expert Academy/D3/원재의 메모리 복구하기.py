# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

# My Solution:
answer = []
for i in range(int(input())):
    origin = input()
    flag = origin[0]
    cnt = 0
    if flag == '1':
        cnt += 1

    for c in origin:
        if c == flag:
            continue
        else:
            cnt += 1
            flag = c
    answer.append(cnt)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
