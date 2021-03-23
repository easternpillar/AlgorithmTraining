# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWEbPukqySUDFAWs&categoryId=AWEbPukqySUDFAWs&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

# My Solution:
for i in range(int(input())):
    N = int(input())
    s1 = (N * (N + 1)) // 2
    s2 = (N * (N + 1)) - N
    s3 = (N * (N + 1))
    print("#{} {} {} {}".format(i + 1, s1, s2, s3))
