# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9

# My Solution:
def light(height, building):
    highest = max(max(heights[building + 1:building + 3]),max(height[building-2:building]))
    if highest >= height[building]:
        return 0
    else:
        return height[building] - highest


answer = []
for i in range(10):
    tn = int(input())
    heights = list(map(int, input().split()))
    tot = 0
    for j in range(2,len(heights)-2):
        tot += light(heights, j)

    answer.append(tot)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
