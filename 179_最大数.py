#!/usr/bin/python
# -*- coding: utf-8 -*-

# 我的方法
class LargeNum(str):
    def __lt__(self, y):
        return self+y > y+self

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(i) for i in nums]
        result = (''.join(sorted(nums, key=LargeNum))).lstrip('0')
        if not result:
            return '0'
        else:
            return result


# 官方解答
class LargerNumKey(str):
    def __lt__(self, y):
        return self+y > y+self
        
class Solution1:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


# 后来经过探索，得出一种更利于理解的方法：
def cmp(x, y):
    # 注意这里是倒序，所以小的反而大
    if x+y < y+x:
        return 1
    if x+y > y+x:
        return -1
    return 0

class MySolution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(i) for i in nums]
        result = (''.join(sorted(nums, cmp)))
        return '0' if result[0] == '0' else result


s = MySolution()

print s.largestNumber([10,2])