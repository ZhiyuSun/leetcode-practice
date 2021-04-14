"""
 f(x) 是 x! 末尾是 0 的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 ）

例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。给定 K，找出多少个非负整数 x ，能满足 f(x) = K 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.14 太难了，不是我能做出来的
class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def zeta(x):
            return x//5 + zeta(x//5) if x > 0 else 0

        lo, hi = K, 10*K + 1
        while lo < hi:
            mi = (lo + hi) // 2
            zmi = zeta(mi)
            if zmi == K: return 5
            elif zmi < K: lo = mi + 1
            else: hi = mi

        return 0
