"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2020.08.16
# BFS，靠自己写出来了，有被感动到
from typing import List
import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {
            '1': '!@#',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        queue = []
        for c in digits:
            ch = num_map[c]
            if not queue:
                for i in ch:
                    queue.append(i)
            else:
                for _ in range(len(queue)):
                    cur = queue.pop(0)
                    for i in ch:
                        queue.append(cur+i)
        return queue    

# 自己把dfs的方法也摸索出来了，厉害
class Solutionmy:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {
            '1': '!@#',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def _dfs(cur, data):
            if not cur:
                return data
            ch = cur[0]
            new_data = []
            nums = num_map.get(ch)
            if data:
                for i in nums:
                    new_data.extend([k + i for k in data])
            else:
                for i in nums:
                    new_data.append(i)
            return _dfs(cur[1:], new_data)

        return _dfs(digits, [])


# 官方解答，回溯法，很值得一学
class Solutionbacktrack:
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
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


# 奇技淫巧之python一行解法
class Solutiononeline:
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

        groups = (phoneMap[digit] for digit in digits)
        return ["".join(combination) for combination in itertools.product(*groups)]
