"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

进阶：

你能在线性时间复杂度内解决此题吗？

 

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

"""
# 暴力法
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []
        
        return [max(nums[i:i + k]) for i in range(n - k + 1)]

# 民间大神版
from typing import List
from collections import deque

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)


        # 特判
        if size == 0:
            return []
        # 结果集
        res = []
        # 滑动窗口，注意：保存的是索引值
        window = deque()


        for i in range(size):
            # 当元素从左边界滑出的时候，如果它恰恰好是滑动窗口的最大值
            # 那么将它弹出
            if i >= k and i - k == window[0]:
                window.popleft()


            # 如果滑动窗口非空，新进来的数比队列里已经存在的数还要大
            # 则说明已经存在数一定不会是滑动窗口的最大值（它们毫无出头之日）
            # 将它们弹出
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)


            # 队首一定是滑动窗口的最大值的索引
            if i >= k - 1:
                res.append(nums[window[0]])
        return res