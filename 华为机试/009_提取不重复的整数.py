"""
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
"""

# 2021.03.06 终于开窍一次
def solution():
    s = input()
    s_list = list(s)
    s_list.reverse()
    res = ''
    visited = set()
    for i in s_list:
        if i not in visited:
            res += i
            visited.add(i)

    return res
           
print(solution())

# 2021.03.06 字符串倒序的优化版
def solution1():
    s = input()
    s = s[::-1]
    res = ''
    visited = set()
    for i in s:
        if i not in visited:
            res += i
            visited.add(i)

    return res
           
print(solution1())