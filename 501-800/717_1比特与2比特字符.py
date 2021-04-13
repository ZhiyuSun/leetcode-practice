"""
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。

示例 1:

输入: 
bits = [1, 0, 0]
输出: True
解释: 
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
示例 2:

输入: 
bits = [1, 1, 1, 0]
输出: False
解释: 
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.13 请叫我，递归之王
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        def _dfs(last, rest):
            if not rest:
                if len(last) == 2:
                    return True
                return False
            if rest[0] == 0:
                if _dfs('0', rest[1:]):
                    return True
            else:
                if _dfs('10', rest[2:]):
                    return True
            return False
        return not _dfs('', bits)


# 2021.04.13 其实这题可以很简单
class Solution2:
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

class Solution3:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        #开始索引
        index = 0
        #标志
        flag = True
        while index < len(bits):
            if bits[index] == 1:
                #为1的话要进两位，标志设为False
                flag = False
                index += 2
            else:
                #为0的话要进一位，标志设为True
                flag = True
                index += 1
        #返回结束时候的标志位
        return flag
