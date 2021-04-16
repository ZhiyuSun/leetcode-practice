"""
给你一个餐馆信息数组 restaurants，其中  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]。你必须使用以下三个过滤器来过滤这些餐馆信息。

其中素食者友好过滤器 veganFriendly 的值可以为 true 或者 false，如果为 true 就意味着你应该只包括 veganFriendlyi 为 true 的餐馆，为 false 则意味着可以包括任何餐馆。此外，我们还有最大价格 maxPrice 和最大距离 maxDistance 两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值。

过滤后返回餐馆的 id，按照 rating 从高到低排序。如果 rating 相同，那么按 id 从高到低排序。简单起见， veganFriendlyi 和 veganFriendly 为 true 时取值为 1，为 false 时，取值为 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.16 我自己做出来了，感觉这题不配做中等题
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        for i in restaurants:
            if veganFriendly == 1 and i[2] != 1:
                continue
            if i[3] > maxPrice:
                continue
            if i[4] > maxDistance:
                continue
            res.append(i)
        # res.sort(key=lambda x: x[1], reverse=True)
        res.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [i[0] for i in res]