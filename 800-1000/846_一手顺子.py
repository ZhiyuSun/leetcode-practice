"""
爱丽丝有一手（hand）由整数数组给定的牌。 

现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。

如果她可以完成分组就返回 true，否则返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hand-of-straights
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List

# 2021.04.08 希望自己能学会Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
