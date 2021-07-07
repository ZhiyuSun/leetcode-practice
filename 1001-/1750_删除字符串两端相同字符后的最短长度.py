"""
给你一个只包含字符 'a'，'b' 和 'c' 的字符串 s ，你可以执行下面这个操作（5 个步骤）任意次：

选择字符串 s 一个 非空 的前缀，这个前缀的所有字符都相同。
选择字符串 s 一个 非空 的后缀，这个后缀的所有字符都相同。
前缀和后缀在字符串中任意位置都不能有交集。
前缀和后缀包含的所有字符都要相同。
同时删除前缀和后缀。
请你返回对字符串 s 执行上面操作任意次以后（可能 0 次），能得到的 最短长度 。

 

示例 1：

输入：s = "ca"
输出：2
解释：你没法删除任何一个字符，所以字符串长度仍然保持不变。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-length-of-string-after-deleting-similar-ends
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.07.07 模拟法即可，直奔题解
class Solution:
    def minimumLength(self, s: str) -> int:
        L, R = 0, len(s)-1
        while L < R:
            if s[L] != s[R]:
                break
            c = s[L]
            while L <= R and s[L] == c: #指针是虚指
                L += 1
            while L <= R and s[R] == c: #指针是虚指
                R -= 1
        
        return R - L + 1
