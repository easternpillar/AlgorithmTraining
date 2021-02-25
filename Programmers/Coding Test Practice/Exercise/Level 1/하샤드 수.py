# Problem:
# Return whether the number is the Harshad number.

# My Solution:
def solution(x):
    s = 0
    temp = x
    while temp != 0:
        temp, r = divmod(temp, 10)
        s += r

    if x % s == 0:
        return True
    else:
        return False
