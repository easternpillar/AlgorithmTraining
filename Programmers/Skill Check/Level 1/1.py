# Problem:
# Given two arrays, add the values in the same index.

# My Solution:
def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    answer.reverse()
    answer.pop()
    answer.reverse()
    return answer
