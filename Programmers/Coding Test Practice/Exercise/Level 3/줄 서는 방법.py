# Problem:
# Given the number of people in line, return the nth case of lines sorted in ascending order.

# My Solution:
def solution(n, k):
    answer = []
    fact = [1 for i in range(n + 1)]
    fact[1] = 1
    for i in range(2, n + 1):
        fact[i] = i * fact[i - 1]

    ns = [i for i in range(1, n + 1)]

    for i in range(n, 0, -1):
        d, m = divmod(k, fact[i - 1])
        if m != 0:
            answer.append(ns[d])
            ns.remove(ns[d])
        else:
            answer.append(ns[d - 1])
            ns.remove(ns[d - 1])
        k = m
    return answer
