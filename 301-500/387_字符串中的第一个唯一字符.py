"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections

# 2020.08.23 又是直奔题解的一天
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

# 2020.12.23 吃点甜头
from collections import defaultdict
class Solution1:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1 

# 2020.03.30 我要好好反省一下自己，这都不会了
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1 