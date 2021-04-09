"""
给定一个整数数组和一个整数 k，你需要在数组里找到不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。

这里将 k-diff 数对定义为一个整数对 (nums[i], nums[j])，并满足下述全部条件：

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
注意，|val| 表示 val 的绝对值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-diff-pairs-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List
# 2021.04.09 我的解法，在处理k=0时不够优雅
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s = set()
        res = 0
        visited = set()
        for i in nums:
            if k == 0 and i in s and i not in visited:
                res += 1
                visited.add(i)
            if i in s:
                continue
            if i+k in s:
                res += 1
            if i-k in s:
                res += 1
            s.add(i)
        return res


# 2021.04.09 民间解法
class Solution2:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res

# 2021.04.09 民间较为清晰的解法
class Solution3:
    def findPairs(self, nums, k):
        # 这里有一个细节需要注意的是: (1,3)等同于(3,1)
        # 所以我们无需将1,3都存储起来, 只要存储3即可. 因为k是确定的, 导致1也是确定的
        if k < 0:
            return 0
        # s存储遍历的元素, r存储上面注释的3
        s, r = set(), set()
        for n in nums:
            if n + k in s:
                r.add(n + k)
            if n - k in s:
                r.add(n)
            s.add(n)
            
        return len(r)
