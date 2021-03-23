# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5

# My Solution:
answer = []
for i in range(int(input())):
    L, U, X = map(int, input().split())
    if X < L:
        answer.append(L - X)
    elif X > U:
        answer.append(-1)
    else:
        answer.append(0)

for i in range(len(answer)):
    print('#{} {}'.format(i + 1, answer[i]))
