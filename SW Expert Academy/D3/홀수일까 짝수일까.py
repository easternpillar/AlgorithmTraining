# Problem:
# Given a positive integer, print whether it is even or odd.

# My Solution:
T = int(input())
for i in range(T):
    num = (input())
    print("#{}".format(i + 1), end=" ")

    if int(num[-1]) % 2 == 0:
        print("Even")
    else:
        print("Odd")
