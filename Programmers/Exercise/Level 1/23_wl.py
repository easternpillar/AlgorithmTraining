# Problem:
# Return the GCM and the LCM.

# My Solution:
def solution(n, m):
    answer = []

    ucl = [n, m]
    ucl.sort(reverse=True)

    while True:
        if ucl[0] % ucl[1] == 0:
            answer.append(ucl[1])
            break
        ucl[0], ucl[1] = ucl[1], ucl[0] % ucl[1]

    answer.append((n * m) // ucl[1])

    return answer

# Learned:
# 1. Euclidean algorithm: https://en.wikipedia.org/wiki/Euclidean_algorithm
