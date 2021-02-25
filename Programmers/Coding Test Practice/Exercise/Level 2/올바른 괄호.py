# Problem:
# Return whether the brackets are correctly paired or not.

# My Solution:
def solution(s):
    left = 0
    right = 0

    for i in s:
        if i == ')':
            right += 1
        else:
            left += 1
        if right > left:
            return False

    if right != left:
        return False
    return True
