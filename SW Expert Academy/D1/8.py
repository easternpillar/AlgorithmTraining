# Problem:
# Given a string of alphabets, converts each alphabet to a number from 1 to 26.

# My Solution:
string=input()
for i in range(len(string)):
    print(ord(string[i])-64,end=" ")