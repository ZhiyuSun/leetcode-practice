"""
给定一个字符串 s，计算具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是连续的。

重复出现的子串要计算它们出现的次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.26 我自己的解法，中心扩散法
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2: return 0
        count = 0
        for i in range(len(s)-1):
            j = i + 1
            p, q = i, j
            if s[p] == s[q]:
                continue
            count += 1
            while p > 0 and q < len(s)-1:
                if s[p-1] == s[p] and s[q] == s[q+1]:
                    count += 1
                    p -= 1
                    q += 1
                else:
                    break
        return count

# 2021.04.26 相邻值的解法
class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        seq = [0, 1]
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                seq[1] += 1
            else:
                res.append(min(seq))
                seq[0] = seq[1]
                seq[1] = 1
        res.append(min(seq))
        return sum(res)

# 2021.04.26 民间大神，不过思路没懂
class Solution2:
    def countBinarySubstrings(self, s: str) -> int:
        pre, cur, res, prec = 0, 1, 0, s[0]
        for c in s[1:]:
            if c != prec: pre, cur = cur, 1
            else: cur += 1
            if cur <= pre: res += 1
            prec = c
        return res
