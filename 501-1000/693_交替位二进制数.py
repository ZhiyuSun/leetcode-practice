"""
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

 

示例 1：

输入：n = 5
输出：true
解释：5 的二进制表示是：101

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-number-with-alternating-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.29 活用函数bin，找了个软柿子捏
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                return False
        return True

# 2021.03.29 遇到一个位运算用的很6的大神
class Solution2:
    def hasAlternatingBits(self, n: int) -> bool:
        tmp = n^(n>>1)
        return tmp&(tmp+1) == 0
