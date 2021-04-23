"""
给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，计算函数值 f(x) = ax2 + bx + c，请将函数值产生的数组返回。

要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-transformed-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.23 自己的解法，但肯定不是最优解
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []
        for i in nums:
            res.append(a*i*i+b*i+c)
        res.sort()
        return res


# 2021.04.23 要利用数学上抛物线的性质，我没完全看懂
class Solution1:
       def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int):
        if a == 0: 
            if b > 0: return [b*num + c for num in nums]
            return [b*num + c for num in nums[::-1]]
        mid = -b/(2*a)
        p, n = [a*num*num + b*num + c for num in nums if num >= mid], [a*num*num + b*num + c for num in nums[::-1] if num < mid]
        if a < 0:
            p.reverse()
            n.reverse()
        res = []
        i, j = 0, 0
        while i < len(p) and j < len(n):
            if p[i] < n[j]:
                res.append(p[i])
                i +=1
            else:
                res.append(n[j])
                j +=1
        if i == len(p): res += n[j:]
        else: res += p[i:]
        return res
