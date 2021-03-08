"""
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格

输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
"""

# 2021.03.06 直奔题解
def func():
    num = int(input())
 
    def getprime(n):
        i = 2
        while i * i <= n and n >= i:
            while n % i == 0:
                n = n // i
                print(i, end=" ")
            i = i + 1
        if n - 1:
            print(n, end=" ")
    getprime(num)

if __name__ == "__main__":
    func()