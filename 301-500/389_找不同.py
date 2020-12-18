"""
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.08.28 直奔题解，思路很巧
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

# 2020.12.18 我变笨了
from collections import defaultdict
class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1
        for i in s:
            t_dict[i] -= 1
        for k, v in t_dict.items():
            if v > 0:
                return k
                