"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/monotone-increasing-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2020.12.15 直奔题解，话说这个解法真的惊艳
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        ones = 111111111
        result = 0
        for _ in range(9):
            while result + ones > N:
                ones //= 10
            result += ones
        return result
