# Problem:
# Given a balanced parenthesis string, return the result of converting to the correct parenthesis string.
# Condition(s):
# 1: If the input is an empty string, it returns an empty string.
# 2: Separate string w with two "balanced parenthesis strings" u, v. However, u should no longer be separated into a "balanced parenthesis string," and v can be an empty string.
# 3: If the string u is the "correct parenthesis string", do it again from step 1 for the string v.
# 3-1: Attach and return the resulting string after u.
# 4: If the string u is not a "correct parenthesis string", follow the steps below.
# 4-1: Attach '(' to an empty string as the first character.
# 4-2: Attach the resulting string that was recursively performed from step 1 for string v.
# 4-3: Put '' back on.
# 4-4: Remove the first and last characters of u and reverse the parenthesis direction of the remaining strings to back.
# 4-5: Returns the generated string.

# My Solution:

def isRight(string):
    temp = string
    prev = ''
    while temp:
        prev = temp
        temp = temp.replace('()', '')
        if prev == temp:
            return False
    return True


def divide(string):
    lcnt = rcnt = 0
    idx = 0
    u = ''
    v = ''
    while True:
        if idx > len(string) - 1:
            break
        if string[idx] == '(':
            lcnt += 1
        else:
            rcnt += 1
        if lcnt == rcnt:
            if string[:idx + 1]:
                u = string[:idx + 1]
            if string[idx + 1:]:
                v = string[idx + 1:]
            break
        idx += 1
    return u, v


def reverse(string):
    temp = ''
    for s in string:
        if s == '(':
            temp += ')'
        else:
            temp += '('
    return temp


def recur(string):
    if isRight(string):
        return string
    else:
        u, v = divide(string)
        if isRight(u):
            return u + recur(v)
        else:
            return '(' + recur(v) + ')' + reverse(u[1:-1])


def solution(p):
    if not p:
        return p
    else:
        return recur(p)