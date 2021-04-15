"""
编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32 
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.15 吸收前面的思路，终于自己做出来了
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        dp[0] = 1
        index_arr = [0] * len(primes)
        for i in range(1, n):
            dp[i] = min([dp[index_arr[k]] * primes[k] for k in range(len(index_arr))])
            for j in range(len(index_arr)):
                if dp[index_arr[j]] * primes[j] == dp[i]:
                    index_arr[j] += 1
        return dp[-1]