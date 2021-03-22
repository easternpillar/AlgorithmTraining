# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWMedCxalW8DFAXd&categoryId=AWMedCxalW8DFAXd&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    periods = set()
    for j in range(N):
        temp = int(input())
        if temp == 1:
            continue
        flag = False
        for p in periods:
            if (temp - 1) % p == 0:
                flag = True
                break
        if not flag:
            periods.add(temp - 1)

    print("#{} {}".format(i + 1, len(periods)))
