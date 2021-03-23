# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWD3Y27q3QIDFAUZ&categoryId=AWD3Y27q3QIDFAUZ&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6

# My Solution:
answer = [1 for _ in range(100)]

for i in range(3, len(answer)):
    answer[i] = answer[i - 2] + answer[i - 3]
for i in range(int(input())):
    N = int(input())
    print("#{} {}".format(i + 1, answer[N + 1]))
