"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

"""
import collections

# 2021.04.19 磕磕绊绊
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        i, j = 0, 0
        dic1 = collections.Counter(s1)
        dic2 = collections.Counter()
        while j < len(s1):
            dic2[s2[j]] += 1
            j += 1
        while j <= len(s2):
            if dic1 == dic2:
                return True
            if j < len(s2):
                dic2[s2[i]] -= 1
                if dic2[s2[i]] == 0:
                    del dic2[s2[i]]
                dic2[s2[j]] += 1
            i += 1
            j += 1
        return False

# 2021.04.19 负明雪烛的解法
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
 # 统计 s1 中每个字符出现的次数
        counter1 = collections.Counter(s1)
        N = len(s2)
        # 定义滑动窗口的范围是 [left, right]，闭区间，长度与s1相等
        left = 0
        right = len(s1) - 1
        # 统计窗口s2[left, right - 1]内的元素出现的次数
        counter2 = collections.Counter(s2[0:right])
        while right < N:
            # 把 right 位置的元素放到 counter2 中
            counter2[s2[right]] += 1
            # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
            if counter1 == counter2:
                return True
            # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
            counter2[s2[left]] -= 1
            # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            # 窗口向右移动
            left += 1
            right += 1
        return False

