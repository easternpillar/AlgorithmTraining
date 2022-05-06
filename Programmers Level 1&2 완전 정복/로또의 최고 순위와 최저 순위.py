# 링크: https://programmers.co.kr/learn/courses/30/lessons/77484
# 문제 접근
# 1. 교집합 갯수 + 0의 갯수=최고 순위
# 2. 교집합 갯수=최저 순위

def solution(lottos, win_nums):
    cnt = len(set(lottos).intersection(set(win_nums)))
    maxi = cnt + lottos.count(0)
    if maxi < 2:
        maxi = 6
    else:
        maxi = 7 - maxi
    if cnt < 2:
        cnt = 6
    else:
        cnt = 7 - cnt
    return [maxi, cnt]
