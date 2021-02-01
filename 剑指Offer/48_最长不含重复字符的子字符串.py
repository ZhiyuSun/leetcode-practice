"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.01.26 双端队列的思想
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

# 2021.02.01 我居然写出来了
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        i, j = 0, 0
        tmp = { s[0] }
        res = 1
        while j < len(s) - 1:
            j += 1
            if s[j] in tmp:
                while i < j:
                    if s[i] == s[j]:
                        tmp.remove(s[i])
                        i += 1
                        break
                    else:
                        tmp.remove(s[i])
                        i += 1
                tmp.add(s[j])
            else:
                tmp.add(s[j])
                res = max(res, len(tmp))
        return res


# 总结优化方向：
# 我移动的是右指针，然后移动左指针
# 其实可以移动左指针，看右指针能移动多远