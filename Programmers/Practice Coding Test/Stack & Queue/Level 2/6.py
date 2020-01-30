# Problem:
# Given a sequence of stock price change, return how long the stock price didn't decrease.

# My Solution:
def solution(prices):
    length = len(prices)
    answer = []

    for i in range(length - 1):
        temp = prices[i]
        time = 0
        for j in range(i + 1, length):
            if prices[j] >= temp:
                time = time + 1
            else:
                time = time + 1
                break
        answer.extend([time])
    answer.extend([0])
    return answer
