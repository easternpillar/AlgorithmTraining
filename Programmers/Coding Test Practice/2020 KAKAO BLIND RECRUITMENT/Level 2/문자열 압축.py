# Problem:
# Given a string, return the length of the shortest string expressed by cutting and compressing the string in more than one unit.

# My Solution:
def compress(string, unit):
    comp = ""
    cnt = 1
    for idx in range(0, len(string), unit):
        temp = string[idx:idx + unit]
        if string[idx + unit:idx + unit + unit] == temp:
            cnt += 1
        else:
            if cnt == 1:
                comp += temp
            else:
                comp += str(cnt) + temp
                cnt = 1
    return len(comp)


def solution(s):
    len_list = []
    if len(s) == 1:
        return 1

    for u in range(1, len(s) // 2 + 1, 1):
        len_list.append(compress(s, u))

    return min(len_list)