"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        s = str(x)
        begin,end = 0, len(s)-1
        while begin < end:
            if s[begin] == s[end]:
                begin += 1
                end -= 1
            else:
                return False
        return True

# 7月份写的
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        a = str(x)
        left, right = 0, len(a) - 1
        while left < right:
            if a[left] != a[right]:
                return False
            left += 1
            right -= 1
        return True

# 数学方法
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10