# Problem:
#

# My Solution:
def solution(n, arr1, arr2):
    answer = []
    b = [0 for i in range(n)]
    for i in range(n):
        b[i] = b[i] | arr1[i]
        b[i] = b[i] | arr2[i]
        b[i] = bin(b[i])

    for i in range(len(b)):
        string = ""
        cnt = 0
        for j in range(len(b[i]) - 1, 1, -1):
            if b[i][j] == '1':
                string += '#'
                cnt += 1
            else:
                string += ' '
                cnt += 1
        while cnt < n:
            string += ' '
            cnt += 1
        answer.append(string)

    for i in range(len(answer)):
        temp = list(answer[i])
        temp.reverse()
        answer[i] = "".join(temp)
    return answer

# Learned:
# 1. bin(), ox(), hex(): converts an integer into a binary number. oct() for octal number, hex() for hexadecimal number.
# 2. rjust(), ljust(): right/left alignment.
# 3. replace(): finds value and replaces it.