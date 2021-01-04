"""
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.01.04 搓搓的贪心法
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed: 
            count = 0
        elif len(flowerbed) == 1:
            count = 0 if flowerbed[0] == 1 else 1
        else:
            count = 0
            for i in range(len(flowerbed)-1):
                print(i)
                if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
            if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
                count += 1 
        return count >= n


# 官方解法，只需要获得为1的两个点，然后就可得出中间多少树
class Solution1:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                if count >= n:
                    return True
                prev = i
        
        if prev < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev - 1) // 2
        
        return count >= n
