# Problem:
# Given a list of phone numbers, return true if any phone number is not the part of other phone number's head or false.

# My Solution:
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        temp1 = phone_book[i]
        for j in range(i + 1, len(phone_book)):
            temp2 = phone_book[j]
            answer = False
            for k in range(len(temp1)):
                if temp1[k] != temp2[k]:
                    answer = True
                    break
            if not answer:
                return answer
    return True

# Other Solution(s):
# 1.
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
