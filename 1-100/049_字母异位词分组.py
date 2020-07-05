import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

# 复杂度O(NKlogK)
# s = Solution()
# result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
# print(result)

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            dic[tuple(sorted(s))] = dic.get(tuple(sorted(s)), []) + [s]
        return list(dic.values())


class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

# 复杂度O(NK)