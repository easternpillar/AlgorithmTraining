# Problem:
# Return what day of the week 'a' month 'b' is when January 1, 2016 is Friday.

# My Solution:
def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = -1
    for i in range(a - 1):
        day += days[i]
    day += b
    mod = day % 7

    if mod == 0:
        answer = 'FRI'
    elif mod == 1:
        answer = 'SAT'
    elif mod == 2:
        answer = 'SUN'
    elif mod == 3:
        answer = 'MON'
    elif mod == 4:
        answer = 'TUE'
    elif mod == 5:
        answer = 'WED'
    else:
        answer = 'THU'

    return answer
