"""

你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
"""
from typing import List

# 2021.04.22 完全不会，困难题直接放弃
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        info=list(zip(startTime,endTime,profit))
        info.sort(key=lambda x:x[1])
        n = len(info)
        # dp[i] 表示考虑前i个task, 在第i个task结束时能够获得的最大收益
        dp = [0]*n
        dp[0] = info[0][2]
        for i in range(1,n):
            # 找endtime中小于等于starttime[i]的最大的时间 如果不存在 则最后left等于0
            left, right = 0, i-1
            while left<right:
                mid=(left+right+1)//2
                if info[mid][1]<=info[i][0]: left=mid
                if info[mid][1]>info[i][0]: right=mid-1 
            # 参加第i个兼职收益为info[i][2] 同时 第left个endtime之前也都是可以参加兼职的dp[left]
            # 两种选择：参与第i个兼职info[i][2]+dp[left]或info[i][2] 不参与dp[i-1]
            if info[left][1]<=info[i][0]:
                dp[i] = max(dp[i-1],info[i][2]+dp[left])
            else:
                dp[i] = max(dp[i-1],info[i][2])
        return dp[-1]
                