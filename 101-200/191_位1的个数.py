"""
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


class Solution2:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum+=1
            n &= (n - 1)
        return sum


# 2021.03.29 学会了位运算
class Solution3:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            n = n & (n-1)
            res += 1
        return res