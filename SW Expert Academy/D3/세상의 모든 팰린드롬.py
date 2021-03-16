# Problem:
# Given a string pattern including wildcards, print if there are any palindromes that can be created.

# My Solution:
T=int(input())
for i in range(T):
    string=input()
    left=0
    right=len(string)-1
    answer=True
    while left<right:
        if string[left]==string[right] or string[left]=='?' or string[right]=='?':
            left+=1
            right-=1
        else:
            answer=False
            break

    print("#{}".format(i+1),end=" ")
    if answer:
        print("Exist")
    else:
        print("Not exist")