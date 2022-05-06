# 링크: https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3
# 문제 접근
# 1. 구현

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):

        cnt = 1
        for i in range(2, num + 1, 1):
            if num % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer