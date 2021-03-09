# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWS2dSgKA8MDFAVT&categoryId=AWS2dSgKA8MDFAVT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

# My Solution:
T = int(input())
for i in range(T):
    aud = list(map(int, list(input())))
    tot = aud[0]
    add = 0
    for j in range(1, len(aud)):
        if tot >= j:
            tot += aud[j]
        else:
            add += j - tot
            tot = j + aud[j]

    print("#{} {}".format(i + 1, add))
