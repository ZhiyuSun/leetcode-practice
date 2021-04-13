"""
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

 

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-case-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2021.04.13 我的解法，DFS
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def _dfs(cur, index):
            if index == len(S):
                res.append(cur)
                return
            if S[index].isalpha():
                _dfs(cur+S[index], index+1)
                _dfs(cur+S[index].upper(), index+1)
            else:
                _dfs(cur+S[index], index+1)

        res = []
        S = S.lower()
        _dfs('', 0)
        return res

# 2021.04.13 民间解法
class Solution1:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        res = []
        path = []
        
        def dfs(cur):
            if cur == len(S):
                res.append(''.join(path))
                return
            
            path.append(S[cur])
            dfs(cur + 1)
            path.pop()
            
            if S[cur].isalpha():
                tmp = chr(ord(S[cur]) ^ (1 << 5)) # 大小写转换，ASCII上相差32
                path.append(tmp)
                dfs(cur + 1)
                path.pop()
                
        
        
        dfs(0)
        
        return res