"""
计算字符串最后一个单词的长度，单词以空格隔开。

输入描述:
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述:
输出一个整数，表示输入字符串最后一个单词的长度。

"""

# 2021.03.06 华为用的是ACM模式，写法1
import sys

for line in sys.stdin:
    last = line.strip().split(" ")[-1]
    leng = len(last)
    print(leng)


# 写法2, 这种更常见一点
def solution():        
    in_str = input()
    if len(in_str) > 5000 or len(in_str) == 0:
        raise Exception

    last = in_str.strip().split(" ")[-1]
    leng = len(last)
    return leng
    
print(solution())