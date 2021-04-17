"""
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

 

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import collections

# 2021.04.16 我的解法，还是挺清晰的
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashmap = collections.Counter(deck)
        min_v = min(hashmap.values())
        while min_v > 1:
            if all([v % min_v == 0 for v in hashmap.values()]):
                return True
            min_v -= 1
        return False

# 2021.04.17 官方解法
class Solution1:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N + 1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False
