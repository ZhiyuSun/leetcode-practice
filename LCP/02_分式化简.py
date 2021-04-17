"""
有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？



连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。

 

输入的cont代表连分数的系数（cont[0]代表上图的a0，以此类推）。返回一个长度为2的数组[n, m]，使得连分数的值等于n / m，且n, m最大公约数为1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/deep-dark-fraction
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2021.04.17 直奔题解，完全不会
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n,m = 0, 1
        for a in cont[::-1]:
            n,m = m, (m * a + n)
        return [m, n]
