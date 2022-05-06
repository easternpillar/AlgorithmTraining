# 링크: https://programmers.co.kr/learn/courses/30/lessons/72410
# 문제 접근
# 1. 길이 3~15
# 2. 소문자, 숫자, 빼기, 밑줄, 마침표
# 3. 마침표는 중간에 연속되지 않게 사용

def solution(new_id):
    new_id = new_id.lower()
    temp = ""
    for c in new_id:
        if 'a' <= c <= 'z' or '0' <= c <= '9' or c == '-' or c == '_' or c == '.':
            temp += c
    idx = 0
    tmp = ''
    while idx < len(temp):
        if temp[idx] == '.':
            tmp += temp[idx]
            while idx < len(temp) and temp[idx] == '.':
                idx += 1
        else:
            tmp += temp[idx]
            idx += 1
    temp = tmp
    if temp and temp[0] == '.':
        temp = temp[1:]
    if temp and temp[-1] == '.':
        temp = temp[:-1]
    if not temp:
        temp += 'a'
    if len(temp) >= 16:
        temp = temp[:15]
    while temp and temp[-1] == '.':
        temp = temp[:-1]
    while temp and len(temp) <= 2:
        temp += temp[-1]
    return temp
