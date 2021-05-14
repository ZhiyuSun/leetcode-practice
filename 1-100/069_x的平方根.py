"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import math
# 2021.03.23 数学法，我学不会的
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


# 2021.03.23 学习二分法
class Solution1:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        l, r, ans = 1, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


# 2021.04.29 先找到临界值，再做判断也可以
class Solution2:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right: 
            mid = (left + right) // 2 
            if mid * mid == x: 
                return mid
            elif mid * mid < x: 
                left = mid + 1 
            else: 
                right = mid - 1
        if left * left < x < (left+1)*(left+1):
            return left
        else:
            return left - 1


# 2021.04.29 我在面试时的做法，如果初始边界值这么设，就没问题了
# 很可惜，听天由命了
class Solution3:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        i, j = 0, x
        while i < j:
            # print(i, j)
            if i == j - 1:
                return i
            mid = i + (j-i) // 2
            prod = mid * mid
            if prod == x:
                return mid
            elif prod > x:
                j = mid
            else:
                i = mid
        return i