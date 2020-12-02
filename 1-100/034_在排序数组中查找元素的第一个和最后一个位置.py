"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

"""
from typing import List
# 2020.12.2 能做，但效率未免太差了
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index_list = []
        for i in range(len(nums)):
            if nums[i] == target:
                index_list.append(i)
        if len(index_list) == 0:
            return [-1, -1]
        else:
            return [index_list[0], index_list[-1]]


# 因为是排序好的数组，可以用二分查找
class Solution2:
	def searchRange(self, nums, target):
		if not nums:
			return [-1,-1]
		n = len(nums)
		# 查找第一个和最后一个元素
		def find(is_find_first):
			begin = 0
			end = n-1
			# if和elif的逻辑跟正常的二分查找一样
			while begin<=end:
				mid = begin+(end-begin)//2
				if nums[mid]>target:
					end = mid-1
				elif nums[mid]<target:
					begin = mid+1
				# 找到目标值了，开始定位到第一个和最后一个位置	
				else:
					# 查找第一个和最后一个逻辑很类似，这里用一个变量标记
					# 是查找第一个还是查找最后一个
					if is_find_first:
						# 如果不满足条件，缩小右边界，继续往左边查找
						if mid>0 and nums[mid]==nums[mid-1]:
							end = mid-1
						else:
							return mid
					else:
						# 如果不满足条件，增大左边界，继续往右边查找
						if mid<n-1 and nums[mid]==nums[mid+1]:
							begin = mid+1
						else:
							return mid
			return -1
		return [find(True), find(False)]
