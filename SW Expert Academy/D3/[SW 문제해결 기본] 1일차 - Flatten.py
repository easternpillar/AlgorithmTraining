# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9

# My Solution:
answer=[]
for i in range(10):
    dump=int(input())
    stacks=list(map(int,input().split()))
    for j in range(dump):
        stacks[stacks.index(max(stacks))]-=1
        stacks[stacks.index(min(stacks))]+=1

    answer.append(max(stacks)-min(stacks))

for i in range(len(answer)):
    print("#{} {}".format(i+1,answer[i]))