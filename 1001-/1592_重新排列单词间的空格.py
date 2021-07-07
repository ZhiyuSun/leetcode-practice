"""
给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证 text 至少包含一个单词 。

请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。

返回 重新排列空格后的字符串 。

示例 1：

输入：text = "  this   is  a sentence "
输出："this   is   a   sentence"
解释：总共有 9 个空格和 4 个单词。可以将 9 个空格平均分配到相邻单词之间，相邻单词间空格数为：9 / (4-1) = 3 个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rearrange-spaces-between-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.07.07 模拟法，自己稍微调试一下就出来了
class Solution:
    def reorderSpaces(self, text: str) -> str:
        blank_num = text.count(' ')

        word_list = text.split()
        if len(word_list) == 1:
            return word_list[0] + ' ' * blank_num

        n = blank_num // (len(word_list) - 1)

        rest = blank_num % (len(word_list) - 1)

        s = ''
        for i in word_list[:-1]:
            s += i + n * ' '
        
        s += word_list[-1] + rest * ' ' 
        return s


# 2021.07.07 超简洁Python解法，值得参考
class Solution1:
    def reorderSpaces(self, text: str) -> str:
        c = text.count(" ")
        li = text.strip().split()
        if len(li) == 1:
            return li[0] + " " * c
        s, s1 = divmod(c, len(li) - 1) 
        return (" " * s).join(li)  + " " * s1
