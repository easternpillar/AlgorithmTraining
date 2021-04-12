# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGAylqcdYDFAUo&categoryId=AWXGAylqcdYDFAUo&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9

# My Solution:
for i in range(int(input())):
    N = int(input())
    temp = '1/' + str(N)
    print("#{}".format(i + 1), end=" ")
    for j in range(N):
        print("{}".format(temp), end=" ")
    print()
