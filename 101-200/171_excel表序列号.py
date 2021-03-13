"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)):
            result += (ord(s[i])-64) * (26 ** (len(s)-1-i))
        return result

s = Solution()
print(s.titleToNumber('AB'))


# 民间算法
# 1行
class Solution1(object):
    def titleToNumber(self, s):
        return sum([(ord(s[i]) - ord('A') + 1)*26**(len(s)-i-1) for i in range(len(s))])

# 另外的简洁的写法
import functools
class Solution2:
    def titleToNumber(self, s):
        return functools.reduce(lambda x, y: x * 26 + y, [ord(a) - 64 for a in s ])


class Solution3:
    def titleToNumber(self, s):
        return sum( (ord(a) - 64) * (26 ** i)  for i, a in enumerate(s[::-1]))
