"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2021.04.14 我的奇奇怪怪的做法，但是能成
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        count = nums.count(0)
        s = {nums[0]}
        diff = 0
        for i in range(1, len(nums)):
            if nums[i] != 0:
                if nums[i] in s:
                    return False
                s.add(nums[i])
                diff += nums[i-1] - nums[i] - 1
        return diff <= count

# 2021.04.14 K神太强了，一语中的
# 除大小王外，所有牌 无重复 ；
# 设此 55 张牌中最大的牌为 maxmax ，最小的牌为 minmin （大小王除外），则需满足：max−min<5
class Solution1:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue # 跳过大小王
            ma = max(ma, num) # 最大牌
            mi = min(mi, num) # 最小牌
            if num in repeat: return False # 若有重复，提前返回 false
            repeat.add(num) # 添加牌至 Set
        return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子 

class Solution2:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子
