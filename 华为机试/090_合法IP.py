"""
题目描述
现在IPV4下用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数（因此不需要用正号出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。

现在需要你用程序来判断IP是否合法。

注意本题有多组样例输入。

输入描述:
输入一个ip地址，保证是xx.xx.xx.xx的形式（xx为整数）

输出描述:
返回判断的结果YES or NO
"""
# 2021.03.08 我自己做出来了
def f(s):
    arr = s.split('.')
    if len(arr) != 4: return 'NO'
    for i in arr:
        if not 0 <= int(i) <= 255: return 'NO'
    return 'YES'

while True:
    try:
        s  = input()
        print(f(s))
    except:
        break

# 别人的做法
while True:
    try:
        ip = input()
        c = ip.split('.')
        all = [0, 0, 0, 0]  # 各部分合法性初始为假
        if len(c) != 4:  # 长度只能为4
            print("NO")
        else:
            for i in range(4):
                # ip地址四部分值介于0~255，且每部分值不需要占位（例如：0010.01.002.011不合法）
                if 0 <= int(c[i]) < 256 and len(c[i]) == len(str(int(c[i]))):
                    all[i] = 1
            if all == [1, 1, 1, 1]:  # 检验后四部分都为真，则IP合法性为真
                print("YES")
            else:
                print("NO")
    except:
        break


# 综合版
