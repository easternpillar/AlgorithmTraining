# Problem:
#

# My Solution:
def possible(digit,target):
    global temp
    for i in range(len(temp)-digit):
        if int(temp[i:i+digit+1])==target:
            return True
    return False

T = int(input())
for i in range(T):
    N = int(input())
    global temp
    temp="".join(input().split())
    for j in range(10):
        for k in range(10*j,10*(j+1)):
            if not possible(j,k):
                print("#{} {}".format(i+1,k))

