"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res


class Solution1:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack():
            if len(track) == n:  
                res.append(track[:])
                return
            for i in range(0, n):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack()
                track.remove(nums[i])

        
        n = len(nums)
        res = []
        track = []
        backtrack()
        return res

# 某一天参考别人的解法
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, path):
            if len(nums) == 0:
                res.append(path[:])
                return
            for i in range(len(nums)):
                num = nums[i]
                path.append(num)
                dfs(nums[:i]+nums[i+1:], path)
                path.pop()
        dfs(nums, [])
        return res

# 覃超老师的详细解法
class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self._dfs(0, nums, [])
        return self.res


    def _dfs(self, level: int, nums: List[int], cur: List[int]):
        # terminator
        if level >= len(nums):
            self.res.append(cur)
            return
        # process


        # drill down
        for i in range(len(nums)):
            if nums[i] not in cur:
                new_cur = cur + [nums[i]]
                self._dfs(level+1, nums, new_cur)


        # reverse

# 上面解法的优化
class Solution4:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self._dfs(0, nums, [])
        return self.res


    def _dfs(self, level: int, nums: List[int], cur: List[int]):
        # terminator
        if len(nums) == 0:
            self.res.append(cur)
            return
        # process


        # drill down
        for i in range(len(nums)):
            new_cur = cur + [nums[i]]
            new_nums = nums[0:i] + nums[i+1:]
            self._dfs(level+1, new_nums, new_cur)


        # reverse


# 覃超老师的BFS
class Solution5:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = [[]]
        level = 0
        while queue:
            # popleft node
            l = len(queue)


            for _ in range(l):
                cur = queue.pop(0)
                for j in range(len(nums)):
                    if nums[j] not in cur:
                        new = cur + [nums[j]]
                        queue.append(new)
            level += 1
            if level == len(nums):
                return queue
        return []


# 2020.08.27 自己写的蹩脚做法，太不容易了
class Solutionmy:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traceback(nums_list, cur):
            if not nums_list:
                res.append(cur)
                return
            for i in nums_list:
                new_list = nums_list[:]
                new_cur = cur[:]
                new_list.remove(i)
                new_cur.append(i)
                traceback(new_list, new_cur)

        res = []
        traceback(nums, [])
        return res

# 稍微优化一下
class Solutionmynew:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traceback(nums_list, cur):
            if not nums_list:
                res.append(cur[:])
                return
            for i in nums_list:
                new_list = nums_list[:]
                new_list.remove(i)
                cur.append(i)
                traceback(new_list, cur)
                cur.pop()

        res = []
        traceback(nums, [])
        return res

# 总结，可采用 new_cur = cur + [nums[i]] 去做append并生成新的数组，
# 可使用 new_nums = nums[0:i] + nums[i+1:] 去删除其中的一个元素


# 2020.9.18 已经能自如的使用回溯法
class Solution918:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _backtrace(sol):
            if len(sol) == len(nums):
                res.append(sol[:])
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                used[i] = 1
                _backtrace(sol + [nums[i]])
                used[i] = 0    

        res = []
        used = [0] * len(nums)
        _backtrace([])
        return res


# 2021.01.07 太爱自己了，这都能做出来
class Solution6:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def trace_back(cur, rest):
            if not rest:
                res.append(cur[:])
                return
            for i in range(len(rest)):
                cur.append(rest[i])
                trace_back(cur, rest[0:i] + rest[i+1:len(nums)])
                cur.pop()

        res = []
        trace_back([], nums)
        return res


# 复杂度分析
# 时间复杂度：O(n∗n!)，其中 n 为序列的长度。
# 空间复杂度：O(n)，其中 n 为序列的长度。除答案数组以外，递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，这里可知递归调用深度为 O(n)。

# 2021.02.03 运用递归的思想，写出来了
class Solution7:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def _dfs(cur, arr):
            if len(arr) == 0:
                res.append(cur)
            for i in range(len(arr)):
                _dfs(cur + [arr[i]], arr[0:i] + arr[i+1:])

        res = []
        _dfs([], nums)
        return res