# Problem:
# A maximum of M from the chicken restaurants in the city should be selected, and all the rest of the chicken restaurants should be closed. Write a program to find out how the city's chicken street will be the smallest.

# My Solution:
import itertools

def distance(city,remains):
    r_list=list(remains)

    tot=0
    for i in range(len(city)):
        for j in range(len(city[i])):
            if city[i][j]==1:
                min=9999
                for r in remains:
                    if abs(i-r[0])+abs(j-r[1])<min:
                        min=abs(i-r[0])+abs(j-r[1])
                tot+=min

    return tot


n,m=map(int,list(input().split()))
city=[list(map(int,list(input().split()))) for _ in range(n)]

chk_list=[]
for i in range(len(city)):
    for j in range(len(city[i])):
        if city[i][j]==2:
            chk_list.append([i,j])

if len(chk_list)-m<=0:
    print(distance(city,set(map(tuple,(chk_list)))))
else:
    answer=set()
    for removes in list(map(list,itertools.combinations(chk_list,len(chk_list)-m))):
        remains=set(map(tuple,(chk_list)))-set(map(tuple,removes))
        answer.add(distance(city,remains))

    print(min(answer))

# Learned:
# 1. set(): can only have an immutable parameter.