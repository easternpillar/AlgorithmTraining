# Problem:
# Given a string consisting of b, d, p, q, print the mirrored string.

# My Solution:
T = int(input())
for i in range(T):
    string = list(reversed(list(input())))
    for j in range(len(string)):
        if string[j] == 'b':
            string[j] = 'd'
        elif string[j] == 'd':
            string[j] = 'b'
        elif string[j] == 'p':
            string[j] = 'q'
        elif string[j] == 'q':
            string[j] = 'p'
    print("#{} {}".format(i + 1, "".join(string)))
