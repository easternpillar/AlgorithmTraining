# Problem:
# Make 369 game.
# Condition(s):
# 1. Express applause with -.
# 2. If you clap more than once, print the '-' consecutively.

# My Solution:
N = int(input())

li = [str(i) for i in range(1, N + 1)]
for eli in li:
    claps=eli.count('3')+eli.count('6')+eli.count('9')
    if claps==0:
        print(eli,end=" ")
    elif claps==1:
        print('-',end=" ")
    else:
        print('-'*claps,end=" ")