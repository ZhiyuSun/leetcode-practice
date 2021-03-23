"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2020.08.21 我最开始的方法，超出了时间限制
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1: return 0
        dp = [0] * len(prices)
        for j in range(1, len(prices)):
            for i in range(0, j):
                if prices[i] < prices[j]:
                    dp[j] = max(dp[j], prices[j]-prices[i])
        return max(dp)

# 上面的方法的反思，其实不必用dp，就是普通的暴力，但仍然是超时
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                ans = max(ans, prices[j] - prices[i])
        return ans


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = float('inf')
        for price in prices:
            max_profit = max(max_profit, price-min_profit)
            min_profit = min(price, min_profit)
        return max_profit

# 2021.03.23 超出时间限制，我废了
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        res = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                res = max(prices[j]-prices[i], res)
        return res

# 2021.03.23 一次遍历就行。按正常的思路也是要一次遍历，把思路转换成算法就行
class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = float('inf')
        for i in prices:
            max_profit = max(max_profit, i-min_profit)
            min_profit = min(min_profit, i)
        return max_profit