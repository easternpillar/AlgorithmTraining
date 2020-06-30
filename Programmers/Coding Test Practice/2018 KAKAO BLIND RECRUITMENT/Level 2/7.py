# Problem:
# Given the converted integer number from 0 to n notation, return the t numbers that nth player will say when m players say one by one.

# My Solution:
def solution(n, t, m, p):
    result = ''
    answer = []
    for i in range(m * t):
        q = i
        if q == 0:
            answer.append(q)
            continue
        temp = []
        while q != 0:
            q, r = divmod(q, n)
            if r >= 10:
                temp.append(chr(r + 55))
            else:
                temp.append(r)
        answer.extend(list(reversed(temp)))
    for i in range(0, len(answer), m):
        if len(result) == t:
            break
        result += str(answer[i + p - 1])

    return result
