"""
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

 

示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]

        temp = [None for _ in range(size)]
        res = [0 for _ in range(size)]
        # 索引数组，作用：归并回去的时候，方便知道是哪个下标的元素
        indexes = [i for i in range(size)]

        self.__merge_and_count_smaller(nums, 0, size - 1, temp, indexes, res)
        return res

    def __merge_and_count_smaller(self, nums, left, right, temp, indexes, res):
        if left == right:
            return
        mid = left + (right - left) // 2
        self.__merge_and_count_smaller(nums, left, mid, temp, indexes, res)
        self.__merge_and_count_smaller(nums, mid + 1, right, temp, indexes, res)

        if nums[indexes[mid]] <= nums[indexes[mid + 1]]:
            return
        self.__sort_and_count_smaller(nums, left, mid, right, temp, indexes, res)

    def __sort_and_count_smaller(self, nums, left, mid, right, temp, indexes, res):
        # [left,mid] 前有序数组
        # [mid+1,right] 后有序数组

        # 先拷贝，再合并
        for i in range(left, right + 1):
            temp[i] = indexes[i]

        i = left
        j = mid + 1
        for k in range(left, right + 1):
            if i > mid:
                indexes[k] = temp[j]
                j += 1
            elif j > right:
                indexes[k] = temp[i]
                i += 1
                res[indexes[k]] += (right - mid)
            elif nums[temp[i]] <= nums[temp[j]]:
                indexes[k] = temp[i]
                i += 1
                res[indexes[k]] += (j - mid - 1)
            else:
                indexes[k] = temp[j]
                j += 1
