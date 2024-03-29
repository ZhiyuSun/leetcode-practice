"""
题目描述

把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。

数据范围：0<=m<=10，1<=n<=10。
本题含有多组样例输入。


输入描述:
输入两个int整数

输出描述:
输出结果，int型
"""

# 7 3 有8种
# 0 0 7
# 0 1 6
# 0 2 5
# 0 3 4
# 1 1 5
# 1 2 4
# 1 3 3
# 2 2 3


# 2021.03.06 别人的解法，绝了
# 放苹果分为两种情况，一种是有盘子为空，一种是每个盘子上都有苹果。
# 令(m,n)表示将m个苹果放入n个盘子中的摆放方法总数。
# 1.假设有一个盘子为空，则(m,n)问题转化为将m个苹果放在n-1个盘子上，即求得(m,n-1)即可
# 2.假设所有盘子都装有苹果，则每个盘子上至少有一个苹果，即最多剩下m-n个苹果，问题转化为将m-n个苹果放到n个盘子上即求(m-n，n)
def f(m,n):
    if m<0 or n<0:
        return 0
    elif m==1 or n==1:
        return 1
    else:
        return f(m,n-1)+f(m-n,n)
while True:
    try:
        m,n=map(int,input().split())
        print(f(m,n))
    except:
        break