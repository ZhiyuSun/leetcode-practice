"""
如果正整数可以被 A 或 B 整除，那么它是神奇的。

返回第 N 个神奇数字。由于答案可能非常大，返回它模 10^9 + 7 的结果。

 

示例 1：

输入：N = 1, A = 2, B = 3
输出：2
示例 2：

输入：N = 4, A = 2, B = 3
输出：6
示例 3：

输入：N = 5, A = 2, B = 4
输出：10
示例 4：

输入：N = 3, A = 6, B = 4
输出：8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nth-magical-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from math import gcd

# 2021.04.12 虽行但超时
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        i, j = 1, 1
        res = 0
        for _ in range(n):
            if a * i < b * j:
                res = a*i
                i += 1
            elif a*i > b*j:
                res = b*j
                j += 1
            else:
                res = a * i
                i += 1
                j += 1
        return res


# 2021.04.12 民间大神解法，是我看不懂的，这个解法通过不了。。

import math

class Solution2:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        if a == b:  # A==B的特殊情况
            return a * n % 1000000007
        minNum = min(a, b)
        lcm = (a * b) // math.gcd(a, b)  # 算出最小公倍数
        m = n*a*b // (a+b)  # 根据步骤2的公式算出M
        i = m//a + m//b - m//lcm  # 根据步骤4的公式算出I
        # print(str(lcm) + '---' + str(m) + '---' + str(i))
        if i == n:  # 若I == N，返回M
            return m % 1000000007
        # 当遇到N值较大，且LCM较小时，I和N的差距会较大，如果此时去递增M效率低，可先把I跳跃到离N最近的值
        lcmI = lcm//a + lcm//b - 1  # 先计算出一个LCM段内能被A或B整除的次数
        j = (n - i - 1) // lcmI  # 再计算出I到N最近点之间有几个LCM段
        i += j * lcmI  # I跳跃到离N最近的值
        m += j * lcm  # M跳跃到离结果最近的值
        step = minNum  # 把M初始递增步长设为A、B中较小的值，可提高递增效率
        # print(str(lcm) + '---' + str(m) + '---' + str(i))
        while i < n:  # 开始递增M值
            if i >= n - 2:  # 当I值接近N时，把递增步长缩小为1，防止步长过大错过正确结果
                step = 1
            m += step  # 递增M
            i = m//a + m//b - m//lcm  # 重新计算I
        return m % 1000000007

