"""
一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/frog-jump
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
# 2021.03.30 这种困难题毫无任何思路
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n, s = len(stones), set(stones)
        dp = [set()  for _ in range(n)]
        dp[0].add(0)

        for i in range(n):
            cur = stones[i]
            for j in range(i):
                need = cur - stones[j]
                if need - 1 in dp[j] or need + 1 in dp[j] or need in dp[j]:
                    dp[i].add(need)
        
        return len(dp[-1]) > 0

