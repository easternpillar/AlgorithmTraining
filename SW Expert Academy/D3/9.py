# Problem:
# Given the number of people responding to each of the two questions and the total number of people, print the maximum and minimum number of people who answered both questions.

# My Solution:
T = int(input())
for i in range(T):
    N, A, B = map(int, input().split())
    print("#{}".format(i + 1), end=" ")
    print(min(A, B), end=" ")
    if A + B > N:
        print(A + B - N)
    else:
        print(0)
