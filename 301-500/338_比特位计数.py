"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.04 暴力法，位运算
from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones
        
        bits = [countOnes(i) for i in range(num + 1)]
        return bits

# 2021.03.04 动态规划，这种方法不太看得懂
class Solution1:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits


# 2021.03.29 稍稍有点绕，理解一下就是要减去最近的2的幂
class Solution2:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits

# 2021.03.29 精彩的动态规划
class Solution3:
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i&(i-1)] + 1)
        return bits

# i&(i-1)就是去掉末尾的1

