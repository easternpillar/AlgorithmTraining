# Problem:
# Given Pascal's triangle depth, print Pascal's triangle.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    pascal = [1]
    print("#{}".format(i+1))
    for j in range(N):
        for p in pascal:
            print(p, end=" ")
        pascal.insert(0, 0)
        pascal.insert(len(pascal), 0)
        temp = []
        for k in range(len(pascal) - 1):
            temp.append(pascal[k] + pascal[k + 1])
        pascal = temp
        print("")
