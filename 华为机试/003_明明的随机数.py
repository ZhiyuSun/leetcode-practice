"""
题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据(用于不同的调查)，希望大家能正确处理)。


注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。

当没有新的输入时，说明输入结束。

输入描述:
注意：输入可能有多组数据(用于不同的调查)。每组数据都包括多行，第一行先输入随机整数的个数N，接下来的N行再输入相应个数的整数。具体格式请看下面的"示例"。

输出描述:
返回多行，处理后的结果
"""

# 2021.03.06 这道题要注意第一个输入是排序字符串的长度
import sys
getline = lambda: sys.stdin.readline().strip() #利用lambda定义读取数据函数
line = getline()
while line:
    s = [int(getline()) for i in range(int(line))] #获取随机生成的数字
    a = sorted(list(set(s))) #去重并排序
    for i in a: print(i) #输出多行
    line = getline()


# 2021.03.06 另一种写法，这种写法更简洁，并适合我
while True:
    try:
        n = int(input())
        set1 = set({})
        for i in range(n):
            set1.add(int(input()))

        nums = list(set1)
        nums.sort()
        for i in nums:
            print(i)
    except:
        break

