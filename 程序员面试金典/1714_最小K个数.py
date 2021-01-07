"""
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-k-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.01.07 取巧
# 但我知道这样远远不够，需要向大神多多学习
from typing import List
import heapq
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heap, ans = [], []
        for i in arr:
            heapq.heappush(heap, i)
        for _ in range(k):
            ans.append(heapq.heappop(heap))
        return ans


