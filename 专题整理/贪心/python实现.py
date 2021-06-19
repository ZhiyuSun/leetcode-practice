from typing import List

# 860. 柠檬水找零
class Solution860:
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

# 322. 零钱兑换
class Solution322:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i-c]+1, dp[i])
        return -1 if dp[amount] == MAX else dp[amount]

# 122. 买卖股票的最佳时机 II
class Solution122:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

# 455. 分发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1
        
        return count

# 55. 跳跃游戏、
class Solution55:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

    def canJump1(self, nums: List[int]) -> bool:
        if not nums: return False
        end_reachable = len(nums) - 1
        for i in range(len(nums)-1, -1 , -1):
            if nums[i] + i >= end_reachable:
                end_reachable = i
        return end_reachable == 0

# 45. 跳跃游戏 II
class Solution45:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        max_position, end, step = 0, 0, 0
        for i in range(size-1):
            max_position = max(max_position, i+nums[i])
            if i == end:
                end = max_position
                step += 1
        return step
