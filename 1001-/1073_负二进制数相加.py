"""
给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。

数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。数组形式 的数字也同样不含前导零：以 arr 为例，这意味着要么 arr == [0]，要么 arr[0] == 1。

返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/adding-two-negabinary-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.26 太难了，直接放弃
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1 
        res, carry = [], 0 
        arr1, arr2 = arr1[::-1], arr2[::-1]
        ## 原始arr1 补充前置0使其与arr2等长
        arr1.extend([0] * (len(arr2) - len(arr1)))

        for i in range(len(arr1)):
            cur = arr1[i] + arr2[i] + carry
            if cur > 1:
                carry = -1
                cur -= 2
            elif cur < 0:
                carry = 1
                cur += 2
            else:
                carry = 0
            res.append(cur)

        res.extend([1, 1]) if carry != 0 else 0
        ## 去掉前置0
        while len(res) >= 2 and res[-1] == 0: 
            res.pop()
        return res[::-1]