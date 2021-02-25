# Problem:
# Given a string, return the JadenCase string.

# My Solution:
def solution(s):
    s=s.lower()
    answer=''
    flag=1

    for i in range(len(s)):
        if s[i]==' ':
            flag=1
            answer+=s[i]
            continue
        if flag==1:
            answer+=s[i].upper()
            flag=0
        else:
            answer+=s[i]
    return answer

# Learned:
# 1. .title(): Capitalizes only the first letter.