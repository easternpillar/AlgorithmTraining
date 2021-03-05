# Problem:
# Given a list, Find the index of 'Kim' and return a string "김서방은 (index)에 있다".

# My Solution:
def solution(seoul):
    idx = seoul.index('Kim')
    return "김서방은 %d에 있다" % idx