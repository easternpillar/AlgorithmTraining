# 링크: https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3
# 문제 접근
# 1. 합공식

def solution(price, money, count):
    temp = price * (count * (count + 1) // 2) - money
    return temp if temp >= 0 else 0
