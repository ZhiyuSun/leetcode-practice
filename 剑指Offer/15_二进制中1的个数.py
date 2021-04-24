"""
请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.04.24 灵活运用位运算的减一与
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count


# 2021.04.24 K神思路1，移位
class Solution1:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

# 2021.04.24 K神思路2
class Solution2:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
