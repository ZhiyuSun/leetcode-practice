"""
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

 

示例 1：

输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-number-of-occurrences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from collections import defaultdict
from typing import List
# 2020.10.28 找个软柿子捏
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for i in arr:
            count[i] += 1
        count_set = set()
        for value in count.values():
            if value in count_set:
                return False
            else:
                count_set.add(value)
        return True


# 优化方案：直接比较set的长度
class Solution1:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        sum={}
        for i in arr:
            if i in sum.keys():
                sum[i]+=1
            else:
                sum[i]=1
        return len(sum.values())==len(set(sum.values()))