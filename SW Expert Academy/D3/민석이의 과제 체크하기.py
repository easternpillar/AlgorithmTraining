# Problem:
# Given the number of students and the number of students who submitted the assignment, print the number of students who did not submit the assignment in ascending order.

# My Solution:
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    print("#{}".format(i + 1), end=" ")
    answer = []
    for j in range(1, N + 1):
        if j not in S:
            answer.append(j)

    answer.sort()
    for a in answer:
        print(a, end=" ")
    print()
