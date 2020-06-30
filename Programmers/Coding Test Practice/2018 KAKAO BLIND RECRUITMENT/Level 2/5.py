# Problem:
# Implement LZW (Lempel–Ziv–Welch) compression.

# My Solution:
def solution(msg):
    answer = []
    dic = [chr(i) for i in range(65, 91, 1)]

    left = 0
    right = len(msg)
    while left < len(msg):
        if msg[left:right] in dic:
            answer.append(dic.index(msg[left:right]) + 1)

            if right < len(msg):
                dic.append(msg[left:right + 1])

            left = right
            right = len(msg)
        else:
            right -= 1
    return answer
