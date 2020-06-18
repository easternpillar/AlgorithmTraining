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
def sep(p):
    l = r = 0
    idx = 0
    u = ''
    v = ''
    while idx < len(p):
        if p[idx] == '(':
            l += 1
        else:
            r += 1
        if l == r:
            u = p[:idx + 1]
            v = p[idx + 1:]
            break
        idx += 1
    return u, v


def check(u):
    l = r = 0
    idx = 0
    while idx < len(u):
        if r > l:
            return False
        if u[idx] == '(':
            l += 1
        else:
            r += 1
        idx += 1
    return True


def solution(p):
    answer = ''
    result = ''

    if p == "" or check(p):
        return p
    else:
        u, v = sep(p)

        if check(u):
            result = solution(v)
            return u + result
        else:
            u = list(u[1:-1])
            for i in range(len(u)):
                if u[i] == '(':
                    u[i] = ')'
                else:
                    u[i] = '('
            return '(' + solution(v) + ')' + "".join(u)
