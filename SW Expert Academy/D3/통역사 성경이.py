# Problem:
# Given sentences, print the number of names for each sentence.
# Condition(s):
# 1. The last word in each sentence includes one of the three punctuation marks ‘.’, ‘?’, or ‘!’.
# 2. Sentences are composed of words consisting of upper and lower case letters and numbers with a space between them, except that the last word ends with a punctuation mark.
# 3. Names start with an uppercase alphabet and the rest are words with a lowercase alphabet.

# My Solution:
def isName(string):
    for i in range(len(string)):
        if not string[i].islower():
            return False
    return True


T = int(input())
for i in range(T):
    N = int(input())
    temp = list(input().split())
    print("#{}".format(i + 1), end=" ")

    cnt = [0 for _ in range(N)]
    idx = 0
    for string in temp:
        if string[0].isupper():
            if string[-1] == '!' or string[-1] == '.' or string[-1] == '?':
                if isName(string[1:-1]):
                    cnt[idx] += 1
                idx += 1
            else:
                if isName(string[1:]):
                    cnt[idx] += 1
        else:
            if string[-1] == '!' or string[-1] == '.' or string[-1] == '?':
                idx+=1

    for c in cnt:
        print(c, end=" ")
    print()
