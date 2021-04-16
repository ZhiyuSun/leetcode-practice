"""
我们用一个特殊的字符串 S 来表示一份单词列表，之所以能展开成为一个列表，是因为这个字符串 S 中存在一个叫做「选项」的概念：

单词中的每个字母可能只有一个选项或存在多个备选项。如果只有一个选项，那么该字母按原样表示。

如果存在多个选项，就会以花括号包裹来表示这些选项（使它们与其他字母分隔开），例如 "{a,b,c}" 表示 ["a", "b", "c"]。

例子："{a,b,c}d{e,f}" 可以表示单词列表 ["ade", "adf", "bde", "bdf", "cde", "cdf"]。

请你按字典顺序，返回所有以这种方式形成的单词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/brace-expansion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.16 我的蹩脚解法
class Solution:
    def expand(self, s: str) -> List[str]:
        arr = []
        tmp = []
        flag = False
        for i in range(len(s)):
            if s[i] == ',':
                continue
            if s[i] not in ['{', '}']:
                if flag:
                    tmp.append(s[i])
                else:
                    arr.append(s[i])
            elif s[i] == '{':
                flag = True
                tmp = []
            else:
                flag = False
                arr.append(tmp)
        # print(arr)

        res = []
        def _dfs(index, path):
            if index == len(arr):
                res.append(path)
                return
            if isinstance(arr[index], list):
                for c in arr[index]:
                    _dfs(index+1, path+c)
            else:
                _dfs(index+1, path+arr[index])
        _dfs(0, '')
        return sorted(res)

# 2021.04.16 民间大神解法
class Solution1:
    def expand(self, S: str) :
        def dfs(index, path):
            if index == len_lst:
                self.res.append(path)
                return
            for string in lst[index]:
                dfs(index+1, path+string)

        self.res = []
        index = 0
        length = len(S)
        lst = []
        tmp = ''
        while index < length:
            if S[index] == '{':
                if tmp:
                    lst.append([tmp])
                    tmp = ''
                j = S.find('}', index+1)
                lst.append(S[index+1:j].split(','))
                index = j+1

            else:
                tmp += S[index]
                index += 1
        if tmp:
            lst.append([tmp])
        len_lst = len(lst)
        # print(lst)
        dfs(0, '')
        return sorted(self.res)

# 对于"{a,b}c{d,e}f"
# 只要变成：[['a', 'b'], ['c'], ['d', 'e'], ['f']]