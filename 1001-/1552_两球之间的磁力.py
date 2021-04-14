"""
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。

已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。

给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/magnetic-force-between-two-balls
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2021.04.14 我不太看得懂
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(x: int) -> bool:
            pre = position[0]
            cnt = 1
            for i in range(1, len(position)):
                if position[i] - pre >= x:
                    pre = position[i]
                    cnt += 1
            return cnt >= m

        position.sort()
        left, right, ans = 1, position[-1] - position[0], -1
        while left <= right:
            mid = (left + right) // 2;
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
