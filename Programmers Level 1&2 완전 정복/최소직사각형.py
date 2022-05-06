# 링크: https://programmers.co.kr/learn/courses/30/lessons/86491?language=python3
# 문제 접근
# 1. 명함 정렬
# 2. 최댓값 도출

def solution(sizes):
    answer = 0
    a, b = list(zip(*[list(sorted(size)) for size in sizes]))
    return max(a) * max(b)
