# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV2b9AkKACkBBASw&categoryId=AV2b9AkKACkBBASw&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7

# My Solution:
answer = []

for i in range(int(input())):
    N, A, B = map(int, input().split())
    mini = B * N
    for j in range(1, N + 1):
        k = 1
        while j * k <= N:
            temp = A * abs(j - k) + B * (N - j * k)
            mini = min(mini, temp)
            k += 1
    answer.append(mini)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
