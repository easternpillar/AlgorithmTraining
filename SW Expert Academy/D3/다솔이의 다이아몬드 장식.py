# Problem
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWSNw5jKzwMDFAUr&categoryId=AWSNw5jKzwMDFAUr&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4

# My Solution:
def SecondDistanceDeco(length):
    temp=list('#'*length)
    temp="...".join(temp)
    temp=".."+temp+".."
    print(temp)

def FirstDistanceDeco(length):
    temp=list('#'*(length*2))
    temp='.'.join(temp)
    temp='.'+temp+'.'
    print(temp)

T=int(input())
for i in range(T):
    string=list(input())
    str_len=len(string)
    string=".#.".join(string)
    string="#."+string+".#"

    SecondDistanceDeco(str_len)
    FirstDistanceDeco(str_len)
    print(string)
    FirstDistanceDeco(str_len)
    SecondDistanceDeco(str_len)
