# Problem:
# Given the string(s), print if it is palindrome.

# My Solution:
T = int(input())
for i in range(T):
    string = list(input())
    print("#{}".format(i + 1), end=" ")
    if string == list(reversed(string)):
        print(1)
    else:
        print(0)
