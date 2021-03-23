"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False

"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False

# 2021.03.23 误打误撞，不明不白的二分法
class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid +1
            else:
                r = mid -1
        return False

# 2021.03.23 优化后
class Solution3:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        l, r = 0, num //2
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid +1
            else:
                r = mid -1
        return False
