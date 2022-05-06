# 링크: https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3
# 문제 접근
# 1. 차집합

def solution(numbers):
    x = set([i for i in range(10)])
    return sum(x - set(numbers))
