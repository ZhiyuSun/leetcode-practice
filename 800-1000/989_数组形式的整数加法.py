"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-to-array-form-of-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.19 投机取巧
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ''.join([str(i) for i in num])
        res = int(s) + k
        return [int(i) for i in list(str(res))]

# 2021.04.19 民间巧解
class Solution1:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        while k:
            num[i] += k
            k, num[i] = num[i] // 10, num[i] % 10
            i -= 1

            if i < 0 and k:
                num.insert(0,0)
                i = 0
        return num
