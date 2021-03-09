# Problem:
# Given a string and the positions to put the hyphen, print the final string.

# My Solution:
T = int(input())
for i in range(T):
    string = list(input())
    H = int(input())

    for p in list(map(int, input().split())):
        if p > len(string) - 1:
            string[p - 1] += '-'
        else:
            string[p] = '-' + string[p]

    print("#{} {}".format(i + 1, "".join(string)))
