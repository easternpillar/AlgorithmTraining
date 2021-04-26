# Problem:
#

# My Solution:
import sys
sys.setrecursionlimit(1000000000)

def divide(arr):
    length=len(arr)
    temp=[]
    temp.append((arr[length // 2]))
    temp.append(divide(arr[:length // 2]))
    temp.append(divide(arr[length // 2 + 1:]))
    return temp


K=int(sys.stdin.readline().rstrip())
buildings=list(map(int,sys.stdin.readline().split()))

print(divide(buildings))