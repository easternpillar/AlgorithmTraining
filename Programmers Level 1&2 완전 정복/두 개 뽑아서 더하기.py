# 링크: https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3
# 문제 접근
# 집합으로 변환 후 모든 경우의 수 계산

from itertools import combinations
def solution(numbers):
    return list(sorted(list(set(a+b for a,b in combinations(numbers,2)))))
