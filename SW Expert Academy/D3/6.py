# Problem:
# Given two numbers, print the number of squared palindrome numbers between them.

# My Solution:
TC = int(input())
for i in range(TC):
    first, last = map(int, input().split())
    cnt = 0
    for j in range(first, last + 1):
        temp = list(str(j))
        if temp == list(reversed(temp)):
            temp = j ** 0.5
            if int(temp) == temp:
                temp = list(str(int(temp)))
                if temp == list(reversed(temp)):
                    cnt += 1

    print("#{} {}".format(i + 1, cnt))
