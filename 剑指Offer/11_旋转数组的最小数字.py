"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

"""
from typing import List

# 我的答案，解答错误
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        if len(numbers) == 1: return numbers[0]
        if numbers[right] > numbers[left]: return numbers[left]
        while left <= right:
            mid = (left + right) // 2
            if mid+1 < len(numbers) and numbers[mid] > numbers[mid+1]:
                return numbers[mid+1]
            if mid-1 >= 0 and numbers[mid-1] > numbers[mid]:
                return numbers[mid]
            else:
                if numbers[mid] >= numbers[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        return numbers[0]


# 官方解答
class Solution1:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2  # 防止溢出
            if numbers[pivot] < numbers[high]:
                high = pivot 
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-by-leetcode-s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。