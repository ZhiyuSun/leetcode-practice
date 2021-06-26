from typing import List
import collections
from collections import deque
# 3. 无重复字符的最长子串
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = res = 0
        window_set = set()
        while right < len(s):
            while s[right] in window_set:
                window_set.remove(s[left])
                left += 1
            window_set.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res

# 159. 至多包含两个不同字符的最长子串
class Solution159:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = collections.defaultdict(int)
        left = right = res = 0
        while right < len(s):
            dic[s[right]] += 1
            while len(dic) > 2:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res

# 340. 至多包含 K 个不同字符的最长子串
class Solution340:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dic = collections.defaultdict(int)
        left = right = res = 0
        while right < len(s):
            dic[s[right]] += 1
            while len(dic) > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res

# 424. 替换后的最长重复字符
class Solution424:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        ans = left = right = 0
        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(num)
            while right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                maxn = max(num)
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans

# 239. 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)

        # 特判
        if size == 0:
            return []
        # 结果集
        res = []
        # 滑动窗口，注意：保存的是索引值
        window = deque()

        for i in range(size):
            # 当元素从左边界滑出的时候，如果它恰恰好是滑动窗口的最大值
            # 那么将它弹出
            if i >= k and i - k == window[0]:
                window.popleft()

            # 如果滑动窗口非空，新进来的数比队列里已经存在的数还要大
            # 则说明已经存在数一定不会是滑动窗口的最大值（它们毫无出头之日）
            # 将它们弹出
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)

            # 队首一定是滑动窗口的最大值的索引
            if i >= k - 1:
                res.append(nums[window[0]])
        return res