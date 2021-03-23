"""
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

注意：

你可以假设胃口值为正。
一个小朋友最多只能拥有一块饼干。

示例 1:

输入: [1,2,3], [1,1]

输出: 1

解释: 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

"""
from typing import List

# 我的解法
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
            g.sort()
            s.sort()
            count = 0
            for i in g:
                if not s:
                    return count
                for k in range(s):
                    if s[k] >= i:
                        s.remove(s[k])
                        count += 1
                        break
            return count


# 双指针法
class Solution1:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
            g.sort()
            s.sort()
            count = 0
            j = 0
            for i in range(len(s)):
                if j < len(g) and s[i] >= g[j]:
                    count += 1
                    j += 1
            return count

# 别人的一些解法
class Solution2:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
            if not s or not g: return 0
            g.sort()
            s.sort()
            if s[-1] < g[0]: return 0
            count=gi=si=0
            while gi < len(g) and si < len(s):
                if s[si] >= g[gi]:
                    count += 1
                    gi += 1
                si += 1
            return count


# 2021.03.23 都不如以前了，Python耗时太多
class Solution3:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        used = [0] * len(g)
        for i in s:
            for j in range(len(g)):
                if used[j] == 1:
                    continue
                if g[j] <= i:
                    res += 1
                    used[j] = 1
                    break
        return res

# 2021.03.23 参考了以前的做法，只要有思路，就把思路具象化，双指针yyds
class Solution4:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g: return 0
        g.sort()
        s.sort()
        i = j = res = 0
        if s[-1] < g[0]: return res
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                res += 1
                i += 1
                j += 1
            else:
                i += 1
        return res