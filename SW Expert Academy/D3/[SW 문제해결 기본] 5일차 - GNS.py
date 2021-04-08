# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14jJh6ACYCFAYD&categoryId=AV14jJh6ACYCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

# My Solution:
nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
answer = []

for i in range(int(input())):
    tn, n = input().split()
    temp = input().split()
    digits = []
    for t in temp:
        digits.append(nums.index(t))
    digits.sort()

    tmp = []
    for d in digits:
        tmp.append(nums[d])
    answer.append(tmp)

for i in range(len(answer)):
    print("#{}".format(i + 1))
    for j in range(len(answer[i])):
        print("{}".format(answer[i][j]), end=" ")
    print()
