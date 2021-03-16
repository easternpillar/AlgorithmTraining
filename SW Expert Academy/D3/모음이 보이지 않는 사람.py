# Problem:
# Given a string, remove the vowel and print it.

# My Solution:
T = int(input())
moeum = ['a', 'e', 'i', 'o', 'u']
for i in range(T):
    string = input()
    for m in moeum:
        string = string.replace(m, '')
    print("#{} {}".format(i + 1, string))
