# 링크: https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3
# 문제 접근
# 1. 인덱스 돌면서 set에 있으면 변환

def solution(s):
    answer = ''
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    idx = 0
    temp = ''
    while idx < len(s):
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
        else:
            temp += s[idx]
            if temp in nums:
                answer += str(nums.index(temp))
                temp = ''
            idx += 1

    return int(answer)