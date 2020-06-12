# Problem:
# Given a string and a number 'n', Return an encrypted string that pushes each alphabet of one sentence to another by a certain distance.

# My Solution:
def solution(s, n):
    answer = ''

    for a in s:
        if a == ' ':
            answer += a
            continue
        elif ord(a) in range(ord('A'), ord('Z') + 1):
            answer += chr((ord(a) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += chr((ord(a) - ord('a') + n) % 26 + ord('a'))
    return answer
