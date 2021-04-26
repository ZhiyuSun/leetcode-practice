"""
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.26 跟猴子偷桃是一个思路
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 确定二分查找左右边界
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            # need 为需要运送的天数
            # cur 为当前这一天已经运送的包裹重量之和
            need, cur = 1, 0
            for weight in weights:
                if cur + weight > mid:
                    need += 1
                    cur = 0
                cur += weight
            
            if need <= D:
                right = mid
            else:
                left = mid + 1
        
        return left
