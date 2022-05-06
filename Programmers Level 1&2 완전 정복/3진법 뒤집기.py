# 링크: https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3
# 문제 접근
# 1. 3진법 변환 후 str 변환

def solution(n):
    base3 = ''
    while True:
        q, r = divmod(n, 3)
        base3 += str(r)
        n = q
        if q == 0:
            break
    base3 = list(reversed(base3))

    answer = 0
    for i in range(len(base3)):
        answer += 3 ** i * int(base3[i])

    return answer