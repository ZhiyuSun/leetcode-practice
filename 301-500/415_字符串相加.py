"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

 

提示：

num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.17 我自己的做法
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1: return num2
        if not num2: return num1
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = '0' * (len(num2)-len(num1)) + num1
        j = 0
        res = ''
        for i in range(len(num1)-1, -1, -1):
            s = int(num1[i]) + int(num2[i]) + j
            res = str(s % 10) + res
            j = s // 10
        if j > 0:
            res = str(j) + res
        return res


# 2021.04.17 K神，永远的神！
class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
