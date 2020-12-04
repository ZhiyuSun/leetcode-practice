"""
统计所有小于非负整数 n 的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""
# 2020.12.04 我真笨
class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[]
        flag=[True]*n
        for i in range(2,n):
            if flag[i]:
                prime.append(i)
            for j in prime:
                if i*j>=n:
                    break
                flag[i*j]=False
                if i%j==0:
                    break
        return len(prime)
