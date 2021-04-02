"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-characters-by-frequency
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from collections import defaultdict
# 2021.04.01 我的一行解法，可惜超时了
class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(sorted(list(s), key=lambda x: (s.count(x), s.index(x)), reverse=True))

# 2021.04.01 我的做法，可以通过
class Solution1:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(int)
        for i in s:
            dic[i] += 1
        tup = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        s = ''
        for i, n in tup:
            s += i * n
        return s

# 2021.04.01 不超时的一行解法
class Solution2:
    def frequencySort(self, s: str) -> str:
        # Counter
        return ''.join([i * j for i, j in collections.Counter(s).most_common()])

# 2021.04.01 桶排序的方法
class Solution3:
    def frequencySort(self, s: str) -> str:
        # 桶排序
        ret = []
        countFrequency = collections.defaultdict(int)
        for i in s:
            countFrequency[i] += 1
        buckets = [[] for _ in range(len(s) + 1)]
        for i in countFrequency:
            buckets[countFrequency[i]].extend(i*countFrequency[i])
        for i in buckets[::-1]:
            if(i):
                ret.extend(i)
        return ''.join(ret)
