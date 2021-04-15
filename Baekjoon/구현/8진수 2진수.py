# Problem:
# Given a octal number, print the number converted into binary number.

# My Solution:
import sys

num = int(sys.stdin.readline().rstrip(), 8)
print(str(bin(num))[2:])