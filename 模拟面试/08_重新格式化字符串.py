"""
给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。

请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。
"""

# 2021.04.08 我的解法，利用奇偶性
class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        chs = []
        for i in s:
            if i.isalpha():
                nums.append(i)
            else:
                chs.append(i)
        res = ''
        if abs(len(nums)-len(chs)) < 2:
            if len(nums) < len(chs):
                chs, nums = nums, chs
            l = len(nums) + len(chs)
            for i in range(l):
                if i % 2 == 0:
                    res += nums[i//2]
                else:
                    res += chs[i//2]
            return res
        return ""
