"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def plusOne(self, digits):
        a = ''
        for i in digits:
            a += str(i)
        return list(map(int, str(int(a)+1)))


# 2020.11.5 温习一下，一般的题目确实南不了我
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join([str(item) for item in digits])
        new_number = int(number) + 1
        return [int(item) for item in str(new_number)]

# 2020.11.5 数学解法了解一下
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_digits = len(digits)
        for i in range(len_digits-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits


# 2021.03.20 取巧法
class Solution3:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(i) for i in digits]))
        num += 1
        return [int(i) for i in str(num)]


# 经验总结，数学法可以重点回忆一下