"""
连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

输入描述:
连续输入字符串(输入多次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组
"""

# 2021.03.06 有感觉了，我一开始的做法
while True:
    try:
        s = input()
        if len(s) <= 8:
            s = s + '0' * (8-len(s))
            print(s)
        else:
            i = 0
            while i < len(s):
                cur = s[i:i+8]
                i = i + 8
                cur = cur + '0' * (8-len(cur))
                print(cur)
    except:
        break


