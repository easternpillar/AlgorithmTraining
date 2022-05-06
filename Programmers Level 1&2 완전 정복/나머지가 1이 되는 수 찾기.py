# 링크: https://programmers.co.kr/learn/courses/30/lessons/87389?language=python3
# 문제 접근
# 1. 브루트 포스

def solution(n):
    for i in range(2, n + 1, 1):
        if n % i == 1:
            return i
