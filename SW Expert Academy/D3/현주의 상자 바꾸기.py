# Problem:
# Given a range of boxes that the numbers of boxes to be converted into the number of rounds every round, print the final numbers of boxes.

# My Solution:
T=int(input())
for i in range(T):
    N,Q=map(int,input().split())

    boxes=[0 for _ in range(N)]
    for j in range(Q):
        L,R=map(int,input().split())
        for l in range(L-1,R,1):
            boxes[l]=j+1

    print("#{}".format(i + 1), end=" ")
    print(*boxes)
