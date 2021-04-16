"""
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

 

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sums-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import collections
from typing import List

# 2021.04.16 我的解法，前缀和+哈希表，超清晰
# 要运用同余定理
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        total = res = 0
        for i in A:
            total += i
            mod = total % K
            res += dic[mod]
            dic[mod] += 1
        return res