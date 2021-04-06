# Problem:
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

# My Solution:
decryption = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
              '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def Data_Extraction(Scanner):
    global N, M, Data
    for y in range(N):
        for x in range(M - 1, -1, -1):
            if Scanner[y][x] == '1':
                Data = Scanner[y][x - 55:x + 1]
                return Data


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    Scanner = [input() for _ in range(N)]
    Data = ''
    Data_Extraction(Scanner)

    result = []
    start_i = 0
    end_i = 6
    for _ in range(8):
        result.append(decryption[Data[start_i:end_i + 1]])
        start_i += 7
        end_i += 7

    value = (result[0] + result[2] + result[4] + result[6]) * 3 + \
            (result[1] + result[3] + result[5]) + result[7]

    if not value % 10:
        print('#%d %d' % (tc, sum(result)))
    else:
        print('#%d %d' % (tc, 0))
