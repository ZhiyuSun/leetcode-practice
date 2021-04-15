"""
给你三个正整数 a、b 和 c。

你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算   a OR b == c  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.15 直奔题解，需要熟练移位的方法
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            bit_a, bit_b, bit_c = (a >> i) & 1, (b >> i) & 1, (c >> i) & 1
            if bit_c == 0:
                ans += bit_a + bit_b
            else:
                ans += int((bit_a + bit_b) == 0)
        return ans

