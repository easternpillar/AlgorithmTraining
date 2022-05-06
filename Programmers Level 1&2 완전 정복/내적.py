# 링크: https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3
# 문제 접근
# 1. 식 적용

def solution(a, b):
    return sum(x*y for x,y in zip(a,b))