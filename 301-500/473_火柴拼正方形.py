"""
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:

输入: [1,1,2,2,2]
输出: true

解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matchsticks-to-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.09 微软遇到的面试题，但是我没做出来
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        s = sum(nums)
        if s % 4 != 0: return False
        w = s // 4
        def _dfs(nums, w_arr):
            if not nums:
                result = True
                for i in w_arr:
                    if i != 0:
                        result = False
                return result
            result = False
            for i in range(len(nums)):
                for j in range(len(w_arr)):
                    if j > 0 and w_arr[j] == w_arr[j-1]:
                        continue
                    if w_arr[j] >= nums[i]:
                        w_arr[j] -= nums[i]
                        if _dfs(nums[:i] + nums[i+1:], w_arr[:]):
                            return True
                        w_arr[j] += nums[i]
            return result

        return _dfs(nums, [w,w,w,w])


# 2021.04.09 官方解法，深度优先搜索
class Solution1:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # If there are no matchsticks, then we can't form any square
        if not nums:
            return False

        # Number of matchsticks we have
        L = len(nums)

        # Perimeter of our square (if one can be formed)
        perimeter = sum(nums)

        # Possible side of our square.
        possible_side =  perimeter // 4

        # If the perimeter can be equally split into 4 parts (and hence 4 sides, then we move on).
        if possible_side * 4 != perimeter:
            return False

        # Reverse sort the matchsticks because we want to consider the biggest one first.
        nums.sort(reverse=True)

        # This array represents the 4 sides and their current lengths
        sums = [0 for _ in range(4)]

        # Our recursive dfs function.
        def dfs(index):

            # If we reach the end of matchsticks array, we check if the square was formed or not
            if index == L:
                # If 3 equal sides were formed, 4th will be the same as these three and answer should be True in that case.
                return sums[0] == sums[1] == sums[2] == possible_side

            # The current matchstick can belong to any of the 4 sides (provided their remaining lenghts are >= the size of the current matchstick)
            for i in range(4):
                # If this matchstick can fir in the space left for the current side
                if sums[i] + nums[index] <= possible_side:
                    # Recurse
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    # Revert the effects of recursion because we no longer need them for other recursions.
                    sums[i] -= nums[index]
            return False        
        return dfs(0)




# 2021.04.09 在综合了别人的种种做法后，我自己做出来了
class Solution3:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        s = sum(nums)
        if s % 4 != 0: return False
        w = s // 4
        def _dfs(index, w_arr):
            if index == len(nums):
                result = True
                for i in w_arr:
                    if i != 0:
                        result = False
                return result
            result = False

            for j in range(len(w_arr)):
                if j > 0 and w_arr[j] == w_arr[j-1]:
                    continue
                if w_arr[j] >= nums[index]:
                    w_arr[j] -= nums[index]
                    if _dfs(index+1, w_arr[:]):
                        return True
                    w_arr[j] += nums[index]
            return result

        return _dfs(0, [w,w,w,w])


# 2021.04.09 再进行优化
class Solution4:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        s = sum(nums)
        if s % 4 != 0: return False
        w = s // 4
        def _dfs(index, w_arr):
            if index == len(nums):
                return all([i==0 for i in w_arr])
            result = False
            for j in range(len(w_arr)):
                if j > 0 and w_arr[j] == w_arr[j-1]:
                    continue
                if w_arr[j] >= nums[index]:
                    w_arr[j] -= nums[index]
                    if _dfs(index+1, w_arr):
                        return True
                    w_arr[j] += nums[index]
            return result

        return _dfs(0, [w,w,w,w])
