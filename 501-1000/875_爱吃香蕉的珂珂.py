"""

"""

# 2021.03.08 直奔题解，但不得不说，这道题很巧妙
# 精华1：使用二分查找
# 精华2：(p-1)//k+1，找到一个堆里面可以吃几次
class Solution:
    def minEatingSpeed(self, piles, H):
        # Can Koko eat all bananas in H hours with eating speed K?
        def possible(K):
            return sum((p-1) // K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
