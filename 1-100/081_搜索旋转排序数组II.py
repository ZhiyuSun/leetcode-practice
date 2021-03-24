"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.24 这道题好难，完全不会，真tm难
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        #如果第一个数和最后一个数不相等，那么跟上一题没有区别
        #如果第一个数和最后一个数相等，而且等于target，return true
        #如果第一个数和最后一个数相等，但是不等于target，在最坏的情况下就需要遍历两个升序数组的某一个，已确定target有可能落在哪一段，极端情况时间复杂度会降低到0(N)
        if not nums:
            return False
        if nums[0] != nums[-1]:
            return self.search1(nums, target)
        if nums[0] == nums[-1]:
            if nums[0] == target:
                return True
            else:
                # for num in nums: #偷懒就可以这么写……直接上O(N)的算法
                #     if num == target:
                #         return True
                # return False
                return self.search2(nums, target)
        
    def search1(self, nums, target): #上一题的解答，两次二分查找分别找旋转点和结果
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return True if nums[0] == target else False
        
        lo, hi = 0, len(nums) - 1
        while(lo <= hi):
            mid = (lo + hi) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid +1]: #旋转点为mid
                break
            if nums[mid] <= nums[-1]:
                hi = mid - 1
            elif nums[mid] >= nums[0]:
                lo = mid + 1
                
        if lo > hi:#没有旋转
            lo, hi = 0, len(nums) - 1
        else:
            if target >= nums[0]:
                lo, hi = 0, mid
            else:
                lo, hi = mid + 1, len(nums) - 1

        while(lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False
    
    def search2(self, nums, target):#这种情况下nums[0] == nums[-1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return True if nums[0] == target else False
        
        lo, hi = 0, len(nums) - 1
        while(lo <= hi):
            mid = (lo + hi) // 2
            if mid + 1 < len(nums) and nums[mid] > nums[mid +1]:
                break
            if nums[mid] == nums[0]: #无法确定mid落在哪一段
                i = mid
                while(i < len(nums) - 1 and nums[i] == nums[i + 1]):
                    i += 1
                if i == len(nums) - 1:#整个右段都找完了，全部跟nums[0]一样，所以target肯定落在左侧，也就是0 ~ mid这一段
                    hi = mid - 1
                else:
                    lo = mid + 1
                
            if nums[mid] < nums[-1]:
                hi = mid - 1
            elif nums[mid] > nums[0]:
                lo = mid + 1    
        if target > nums[mid]:
            return False #因为mid一定是最大的那个数
        elif target == nums[mid]: #找到了就直接返回
            return True
        elif target < nums[mid]: #还需要二分查找，现在要确认找左侧还是找右侧
            if target > nums[0]: #在左侧找
                lo, hi = 0, mid - 1
            else: #在右侧找
                lo, hi = mid + 1, len(nums) - 1
            
        while(lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return False

# 2021.03.24 我的解法，人狠话不多
from typing import List
class Solution2:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
