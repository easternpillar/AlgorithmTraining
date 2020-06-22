# Problem:
# Return the multiplication of the matrix.

# My Solution:
def solution(arr1, arr2):
    answer = []
    arr2 = (list(zip(*arr2)))

    for a in arr1:
        temp = []
        for b in arr2:
            tot = 0
            for i in range(len(a)):
                tot += (a[i] * b[i])
            temp.append(tot)
        answer.append(temp)
    return answer
