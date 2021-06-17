from typing import List

# 78. 子集
class Solution78:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _dfs(cur, index):
            # cur为当前结果，index为遍历的索引
            # 如果遍历索引走到最后了，则存储当前结果
            if index == len(nums):
                res.append(cur[:])
                return
            # 这一步代表使用当前索引的元素
            cur.append(nums[index])
            # 继续递归
            _dfs(cur, index+1)
            # 回溯，把当前元素给弹出
            cur.pop()
            # 继续递归
            _dfs(cur, index+1)

        res = []
        _dfs([], 0)
        return res

# 17. 电话号码的字母组
class Solution17:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                res.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        res = list()
        backtrack(0)
        return res


# 51. N皇后
# 52. N皇后II
class Solution52:
    def __init__(self):
        self.res = 0

    def totalNQueens(self, n: int) -> int:
        col, pie, na = set(), set(), set()
        def _dfs(level):
            if level == n:
                self.res += 1
                return
            for j in range(0, n):
                if j in col or level + j in pie or level -j in na:
                    continue
                col.add(j)
                pie.add(level +j)
                na.add(level-j)
                _dfs(level + 1)
                col.remove(j)
                pie.remove(level +j)
                na.remove(level-j)

        _dfs(0)
        return self.res

# 473. 火柴拼正方形
class Solution473:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0: return False
        width = s // 4
        matchsticks.sort(reverse=True)
        def backtrack(arr, index):
            if index == len(matchsticks) and all([i == 0 for i in arr]):
                return True
            for i in range(len(arr)):
                if i > 0 and arr[i] == arr[i-1]:
                    continue
                if arr[i] >= matchsticks[index]:
                    arr[i] -= matchsticks[index]
                    if backtrack(arr, index+1):
                        return True
                    arr[i] += matchsticks[index]
            return False

        return backtrack([width] * 4, 0)
        