"""
给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。 

请你返回排序后的数组。
"""
from typing import List
from collections import defaultdict

# 2021.04.01 微软面试时遇到了，我的做法
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        order = []
        for i in nums:
            if i not in order:
                order.append(i)
            dic[i] += 1
        order.sort()
        order.reverse()
        for i in range(len(order)):
            for j in range(len(order)-i-1):
                if dic[order[j]] > dic[order[j+1]]:
                    order[j], order[j+1] = order[j+1], order[j]
        res = []
        for i in order:
            for j in range(dic[i]):
                res.append(i)
        return res


# 2021.04.01 别人的做法
# sorted可以分级排序
class Solution1:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = dict()
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        counter = sorted(counter.items(), key=lambda x: (x[1], -x[0]))
        res = []
        for key, value in counter:
            while value:
                res.append(key)
                value -= 1
        return res


# 2021.04.01 别人的一行解法
class Solution2:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: (nums.count(x), -x))

# 2021.04.01 另一位大神的解法
class Solution3:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_count = {}
        return_list = []
        for i in nums:
            if i not in nums_count:
                nums_count[i] = 1
            else:
                nums_count[i] += 1
        # sorted(iterable, cmp=None, key=None, reverse=False),默认递增
        # cmp比较函数（两个参数），key比较元素（一个参数）
        # 根据value递增，key递减
        new_count = sorted(nums_count.items(),key = lambda x:(x[1],-x[0]))
        print(new_count)
        for num in new_count:
            return_list += [num[0]]*num[1]
        return return_list


# 然后就是排序，一般的sorted(dict.items(), key=lambda x: x[1])都会，
# 可以用字典的值进行排序，但是还需要同时按照字典的键进行降序排序，
# 关键就在于lambda x: x[1] 改成 lambda x: (x[1], -x[0])；

# 相似题：
# 451. 根据字符出现频率排序
#