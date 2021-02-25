# Problem:
# Given the length of bridge, the weights of trucks, and the weight the bridge can load,
# return the time all trucks passed the bridge.
# Condition(s):
# 1. The lengths of each truck are all 1.
# 2. It takes 1 sec for a truck to pass length 1.

# My Solution: DENIED
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     List = []
#     for truck in truck_weights:
#         while sum(List[-bridge_length + 1:]) + truck > weight:
#             List.append(0)
#         List.append(truck)
#     answer = len(List) + bridge_length
#     return answer

def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    sec = 0
    while q:
        sec += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec

# Learned:
# 1. addition is more efficient than appending of a list.