"""
给你一个字符串 s ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
"""

# 2021.04.19 我的做法，超时了
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if len(set(list(s[i:j+1]))) == 3:
                    res += 1
        return res

# 2021.04.19 这个思路太秀了，只要此时找到，一直到后面剩下的，都是
class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt_a = 0
        cnt_b = 0
        cnt_c = 0

        res = 0
        L = 0
        for R in range(n):
            if s[R] == 'a':     cnt_a += 1
            if s[R] == 'b':     cnt_b += 1
            if s[R] == 'c':     cnt_c += 1

            while cnt_a >= 1 and cnt_b >= 1 and cnt_c >= 1:
                res += (n - R)                  #与右侧剩下的，可以组成合法的情况（R也是合理的）

                if s[L] == 'a':     cnt_a -= 1
                if s[L] == 'b':     cnt_b -= 1
                if s[L] == 'c':     cnt_c -= 1
                L += 1
        return res
