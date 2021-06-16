from typing import List

# 70. 爬楼梯

# 22. 括号生成
class Solution22:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def _dfs(left, right, path):
            if left == right == 0:
                res.append(path)
                return
            if left > 0:
                _dfs(left-1, right, path + '(')
            if right > left:
                _dfs(left, right-1, path + ')')
        _dfs(n, n, '')
        return res

    def generateParenthesis1(self, n: int) -> List[str]:
        def traceback(left, right, cur):
            if left == right == n:
                res.append(''.join(cur))
                return
            if left < n:
                cur.append('(')
                traceback(left+1, right, cur)
                cur.pop()
            if right < left and right < n:
                cur.append(')')
                traceback(left, right+1, cur)
                cur.pop()

        res = []
        traceback(0, 0, [])
        return res

    def generateParenthesis2(self, n: int) -> List[str]:
        res, queue = [], []
        queue.append(('',n,n))
        while queue:
            path, left, right = queue.pop(0)
            if left == right == 0:
                res.append(path)
                continue
            if left > 0: queue.append((path+'(', left-1, right))
            if right > left: queue.append((path+')', left, right-1))
        return res

# 77. 组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def _dfs(cur, index):
            if len(cur) == k:
                res.append(cur)
                return
            for i in range(index, n+1):
                _dfs(cur+[i], i+1)
        res = []
        _dfs([], 1)
        return res


# 46. 全排列
class Solution46:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _dfs(cur, rest):
            if not rest:
                res.append(cur)
            for i in range(len(rest)):
                _dfs(cur+[rest[i]], rest[0:i] + rest[i+1:])

        _dfs([], nums)
        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:
        def _dfs(cur):
            if len(cur) == len(nums):
                res.append(cur)
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = 1
                _dfs(cur+[nums[i]])
                used[i] = 0
        res = []
        used = [0]*len(nums)
        _dfs([])
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
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


# 47. 全排列 II