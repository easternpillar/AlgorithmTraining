# Problem:
# Print the N combination R value.

# My Solution: Denied.
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# def combination(n, r):
#     return factorial(n) / factorial(r) / factorial(n - r)
#
#
# answer = []
# for i in range(int(input())):
#     N, R = map(int, input().split())
#     answer.append(int(combination(N, R)) % 1234567891)
#
# for i in range(len(answer)):
#     print("#{} {}".format(i + 1, answer[i]))

# def combination(n,r):
#     if n==r:
#         return 1
#     elif r==1:
#         return n
#     else:
#         return combination(n-1,r-1)+combination(n-1,r)
#
# answer=[]
# for i in range(int(input())):
#     N,R=map(int,input().split())
#     answer.append(combination(N,R)%1234567891)
#
# for i in range(len(answer)):
#     print("#{} {}".format(i+1,answer[i]))

