"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。 

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if i-c>=0 else MAX for c in coins]) + 1
        return -1 if dp[amount] == MAX else dp[amount]


# 2020.10.13 反复解答后，无解


# 2020.10.13 参考了之前的做法，使用动态规划重写本题

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            dp[i] = min(dp[i-c] if i-c >= 0 else MAX for c in coins) + 1
        return -1 if dp[-1] == MAX else dp[-1]


# ps. JAVA代码真是劝退


# 2021.03.21 错误的方法，零钱不一定有1
class Solutionerror:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        count = 0
        for i in coins[::-1]:
            while amount - i >= 0:
                amount -= i
                count += 1
                print(amount)
            if amount == 0:
                return count
        if amount > 0:
            return -1

# 2021.03.21 重温正解
class Solution4:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 

# 2021.04.26 自己做出来了，感动
class Solution5:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i-c]+1, dp[i])
        return -1 if dp[-1] == float("inf") else dp[-1]

# 2021.06.18 重温一下
class Solution6:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i-c]+1, dp[i])
        return -1 if dp[amount] == MAX else dp[amount]