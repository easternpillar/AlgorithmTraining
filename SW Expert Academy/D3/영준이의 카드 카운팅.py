# Problem:
# Given the spade, diamond, heart, and clover card numbers, print the number of missing numbers for each card type.

# My Solution:
T = int(input())
for i in range(T):
    h = set()
    s = set()
    c = set()
    d = set()
    temp = input()
    idx = 0
    flag = True
    while True:
        if idx > len(temp) - 1:
            break
        if temp[idx] == 'S':
            if temp[idx + 1:idx + 3] in s:
                flag = False
                break
            s.add(temp[idx + 1:idx + 3])
        elif temp[idx] == 'D':
            if temp[idx + 1:idx + 3] in d:
                flag = False
                break
            d.add(temp[idx + 1:idx + 3])
        elif temp[idx] == 'C':
            if temp[idx + 1:idx + 3] in c:
                flag = False
                break
            c.add(temp[idx + 1:idx + 3])
        elif temp[idx] == 'H':
            if temp[idx + 1:idx + 3] in h:
                flag = False
                break
            h.add(temp[idx + 1:idx + 3])
        idx += 3

    if not flag:
        print("#{} {}".format(i + 1, "ERROR"))

    else:
        print("#{} {} {} {} {}".format(i + 1, 13 - len(s), 13 - len(d), 13 - len(h), 13 - len(c)))
