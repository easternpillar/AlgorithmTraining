# Problem:
# Given a list of 0s or positive integers, return the biggest number that can be made by attaching those.
# Condition(s):
# 1. The range of elements is between 0 and 1000.
# 2. Return the answer with string type.

# My Solution:
def solution(numbers):
    answer = ''
    tempList = []

    for i in range(len(numbers)):
        temp = str(numbers[i])
        temp += temp * 4
        temp = temp[:5]
        tempList.extend([int(temp)])

    zipped = list(zip(tempList, [i for i in range(len(tempList))]))
    zipped.sort(reverse=True)

    for i in range(len(numbers)):
        answer += str(numbers[zipped[i][1]])

    answer = str(int(answer))

    return answer
