# 링크: https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
# 문제 접근
# 1. 2차원 배열

def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    for num in numbers:
        if num % 3 == 1:
            left[0] = num // 3
            left[1] = 0
            answer += 'L'
        elif num != 0 and num % 3 == 0:
            right[0] = num // 3 - 1
            right[1] = 2
            answer += 'R'
        else:
            x, y = 3, 1
            if num != 0:
                x = num // 3
            if abs(left[0] - x) + abs(left[1] - y) < abs(right[0] - x) + abs(right[1] - y):
                left[0] = x
                left[1] = y
                answer += 'L'
            elif abs(left[0] - x) + abs(left[1] - y) > abs(right[0] - x) + abs(right[1] - y):
                right[0] = x
                right[1] = y
                answer += 'R'
            else:
                if hand == 'right':
                    right[0] = x
                    right[1] = y
                    answer += 'R'
                else:
                    left[0] = x
                    left[1] = y
                    answer += 'L'

    return answer