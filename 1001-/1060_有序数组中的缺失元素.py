"""

"""

from typing import List

# 2021.04.26 我的解法
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > k:
                return nums[i] + k
            else:
                k = k - (nums[i+1]-nums[i]-1)
        return nums[-1] + k

# 2021.04.26 线性法
class Solution1:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
                
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 

        idx = 1
        # find idx such that 
        # missing(idx - 1) < k <= missing(idx)
        while missing(idx) < k:
            idx += 1

        # kth missing number is larger than nums[idx - 1]
        # and smaller than nums[idx]
        return nums[idx - 1] + k - missing(idx - 1)

# 2021.04.26 重点是二分法
class Solution2:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
            
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 
        
        left, right = 0, n - 1
        # find left = right index such that 
        # missing(left - 1) < k <= missing(left)
        while left != right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot 
        
        # kth missing number is larger than nums[left - 1]
        # and smaller than nums[left]
        return nums[left - 1] + k - missing(left - 1) 
