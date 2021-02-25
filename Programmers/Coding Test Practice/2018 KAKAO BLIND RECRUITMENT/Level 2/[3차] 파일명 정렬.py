# Problem:
# Given the file names, return the file list sorted by file names.
# Condition(s):
# 1. The filename consists of a string(head), a numeric(number), and a string(tail).
# 2. The sort order is head, number, and tail by ascending.

# My Solution:
def solution(files):
    answer = []
    temp = []
    for i in range(len(files)):
        file = files[i]
        head = ''
        number = ''
        tail = ''
        idx = 0
        flag = 0
        while idx < len(file):
            if file[idx].isdigit():
                number += file[idx]
                flag = 1
            else:
                if flag == 0:
                    head += file[idx]
                else:
                    tail += file[idx:]
                    break
            idx += 1

        temp.append([head.lower(), int(number), tail, i])
    temp.sort(key=lambda x: (x[0], x[1], x[3]))
    for i in range(len(temp)):
        answer.append(files[temp[i][3]])
    return answer
