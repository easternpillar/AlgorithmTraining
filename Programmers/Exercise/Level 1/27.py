# Problem:
# Given a phone number, Return an encrypted number with * except four digits at the end.

# My Solution:
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) - 4):
        answer += '*'
    answer += phone_number[len(phone_number) - 4::]
    return answer
