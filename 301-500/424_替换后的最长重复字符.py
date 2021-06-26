"""
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。

 

示例 1：

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
示例 2：

输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-repeating-character-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.15 滑动窗口，直奔题解
# 有点绕，需要好好理解一下
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])
            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1
        
        return right - left

# 2021.04.15 我写的更易理解的滑动窗口
class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        ans = left = 0
        for right in range(n):
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(num)
            while right - left + 1 - maxn > k:
                num[ord(s[left]) - ord("A")] -= 1
                maxn = max(num)
                left += 1
            ans = max(ans, right - left + 1)

        return ans

# 2021.04.15 继续优化
class Solution2:
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
