# Problem:
# Two trains A and B are running towards each other.
# The front of the two trains is D miles apart, and train A is running at A and B is running at B.
# The fly flies from the front of train A to train B at F speed.
# As soon as flies reach the front of train B, it turns and flies at the same speed toward train A.
# Then, if trains A and B collide, the fly will die. Print the distance traveled before the fly died.

# My Solution:
T = int(input())
for i in range(T):
    D, A, B, F = map(int, input().split())
    print("#{}".format(i + 1), end=" ")
    answer = 0
    t_meet = D / (A + B)
    print(t_meet * F)
