"""
给定一个整数数组 nums 。区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

请你以下标 i （0 <= i <= nums.length ）为起点，元素个数逐次递增，计算子数组内的元素和。

当元素和落在范围 [lower, upper] （包含 lower 和 upper）之内时，记录子数组当前最末元素下标 j ，记作 有效 区间和 S(i, j) 。

求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 有效 区间和的个数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-range-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List
import bisect

# 2021.04.09 我居然自己做出来了
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 1
        res = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            for k, v in dic.items():
                if lower <= s - k <= upper:
                    res += v
            dic[s] += 1
        return res

# 2021.04.09 是我看不懂的写法
class Solution1:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect.bisect_right(pre, now - lower) - bisect.bisect_left(pre, now - upper)
            bisect.insort(pre, now)
        return res
