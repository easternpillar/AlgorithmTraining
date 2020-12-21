# Problem:
# Given an 8-digit date in order of year, month and day, print the date in the format ”YYYY/MM/DD”.
# Condition(s):
# 1. Print -1 if the date is not valid.

# My Solution:
T = int(input())
output = ''
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(T):
    temp = input()
    year = temp[:4]
    month = temp[4:6]
    day = temp[6:]
    if int(month) < 1 or int(month) > 12 or int(day) > days[int(month) - 1] or int(day) < 1:
        print('#{} -1'.format(i + 1))
    else:
        print("#{} {}/{}/{}".format(i + 1, year, month, day))
