# Problem:
# Given strings encoded by base64, print the decoded strings.

# My Solution:
T = int(input())

base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
for i in range(T):
    encoded = input()
    print("#{}".format(i + 1), end=" ")
    for j in range(0, len(encoded), 4):
        bit = 0
        for char in encoded[j:j + 4]:
            bit += base64.index(char)
            bit = bit << 6
        bit = bit >> 6
        for k in range(3):
            temp = bit
            temp = temp << (8 * k)
            temp = temp >> (8 * 2)
            print(chr(0b000000000000000011111111 & int(bin(temp), 2)), end="")
    print("")

# Learned:
# 1. bin(): converts the number into binary number.
