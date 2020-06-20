# Problem:
# Given progresses and speeds to be completed of functions, return the numbers of functions that will be released together.
# Condition(s):
# 1. Functions that are already finished can not be released before pr-progressing functions are released.


# My Solution:
import math


def solution(progresses, speeds):
    answer = []
    tempList = []
    for i in range(len(progresses)):
        tempList.extend([math.ceil((100 - progresses[i]) / speeds[i])])

    init = 0
    for i in range(len(tempList)):
        if tempList[i] > init:
            if init == 0:
                init = tempList[i]
                cnt = 1
            else:
                init = tempList[i]
                answer.extend([cnt])
                cnt = 1
        else:
            cnt = cnt + 1
    answer.extend([cnt])

    return answer
