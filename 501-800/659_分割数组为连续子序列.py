"""
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。

如果可以完成上述分割，则返回 true ；否则，返回 false 。

 

示例 1：

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3
3, 4, 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.12.4 cv大法好
import collections
import heapq
from typing import List
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            queue = mp.get(x - 1)
            if queue:
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)
        
        return not any(queue and queue[0] < 3 for queue in mp.values())


