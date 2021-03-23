# Problem:
# Given the length of the three sides of the rectangle, print the length of the other side.

# My Solution:
answer=[]
for i in range(int(input())):
    temp=list(map(int,input().split()))
    for t in temp:
        if temp.count(t)%2==1:
            answer.append(t)
            break

for i in range(len(answer)):
    print("#{} {}".format(i+1,answer[i]))