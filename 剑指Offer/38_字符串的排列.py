"""
输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""
from typing import List

# 2021.04.02 我的做法，但是有个用例没有过，还是不知道是什么问题
# 后来发现，是s应该替换为order_s，乌龙了
class Solution:
    def permutation(self, s: str) -> List[str]:
        def _dfs(cur, rest):
            if len(cur) == len(s):
                res.append(cur)
                return
            for i in range(len(rest)):
                if i > 0 and rest[i] == rest[i-1]:
                    continue
                _dfs(cur+rest[i], rest[:i] + rest[i+1:])

        order_s = "".join(sorted(s))
        res = []
        _dfs('', order_s)
        return res


# 2021.04.02 别人的做法
class Solution2:
    def permutation(self, s: str) -> List[str]:
        if not s: return 
        s=list(sorted(s))
        res=[]
        def helper(s,tmp):
            if not s: res.append(''.join(tmp))
            for i,char in enumerate(s):
                if i>0 and s[i]==s[i-1]:
                    continue
                helper(s[:i]+s[i+1:],tmp+[char])
        helper(s,[])
        print(len(res))
        return res
