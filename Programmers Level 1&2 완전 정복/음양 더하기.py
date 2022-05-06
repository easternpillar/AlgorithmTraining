# 링크: https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3
# 문제 접근
# 반복문

def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        answer.append(0 + absolutes[i] if signs[i] else 0 - absolutes[i])
    return sum(answer)
