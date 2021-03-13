"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.12 说实在的，我现在还是不懂
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n:
            n -= 1
            s = chr(65 + n % 26) + s
            n //= 26
        return s

"""
思路：
除留余数法
以486为例，10进制转换：
486 // 10^0 % 10 = 6
486 // 10^1 % 10 = 8
486 // 10^2 % 10 = 4

以486为例，2进制转换：
486 // 2^0 % 2 = 0
486 // 2^1 % 2 = 1
486 // 2^2 % 2 = 1
486 // 2^3 % 2 = 0
486 // 2^4 % 2 = 0
486 // 2^5 % 2 = 1
486 // 2^6 % 2 = 1
486 // 2^7 % 2 = 1
486 // 2^8 % 2 = 1

26进制呢


"""


# 2021.03.13 靠自己的力量做出来了
class Solution2:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n > 0:
            n -= 1
            s = chr(65 + n % 26) + s
            n = n // 26
        return s