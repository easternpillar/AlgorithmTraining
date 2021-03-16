# Problem:
# Given a string pattern including wildcards, print if there are any palindromes that can be created.

# My Solution:
T = int(input())
for i in range(T):
    string = input()
    answer = True
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        elif string[left] == '*':
            right -= 1
        elif string[right] == '*':
            left += 1
        else:
            answer = False
            break

    print("#{}".format(i + 1), end=' ')
    if answer:
        print("Exist")
    else:
        print("Not exist")
