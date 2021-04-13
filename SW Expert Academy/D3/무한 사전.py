# Problem:
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXdHwI1aCy0DFAS5

# My Solution:
answer = []
for i in range(int(input())):
    P = input()
    Q = input()
    if P.rstrip() + 'a' == Q.rstrip():
        answer.append('N')
    else:
        answer.append('Y')

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
