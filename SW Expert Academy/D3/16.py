# Problem:
# Given the number of bus routes and the start and end numbers of the bus stops, print the number of bus routes at stop C.

# My Solution:
T = int(input())
for i in range(T):
    line = [0 for _ in range(5001)]
    print("#{}".format(i + 1), end=" ")
    N = int(input())

    for j in range(N):
        start, end = map(int, input().split())
        for k in range(start, end + 1):
            line[k] += 1

    P = int(input())
    for j in range(P):
        C = int(input())
        print("{}".format(line[C]), end=" ")
    print()
