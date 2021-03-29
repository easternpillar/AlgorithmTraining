# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWAe5G8afT0DFAUw&categoryId=AWAe5G8afT0DFAUw&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6

# My Solution:
answer = []
for i in range(int(input())):
    A, B = map(int, input().split())
    q = A // B
    answer.append(q ** 2)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
