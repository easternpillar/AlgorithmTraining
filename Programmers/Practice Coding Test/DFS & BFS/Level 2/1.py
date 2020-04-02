# Problem:
# Given an array of positive integers, return the number of ways that make the target number using only + and -.

# My Solution:
def solution(numbers, target):
    answer = 0
    com = [0]

    for i in range(len(numbers)):
        temp = []
        for j in range(len(com)):
            temp.extend([com[j] + numbers[i], com[j] - numbers[i]])
        com = temp.copy()

    for i in range(len(com)):
        if com[i] == target:
            answer += 1
    return answer
