"""
单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足：

words.length == indices.length
助记字符串 s 以 '#' 字符结尾
对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 words[i] 相等
给你一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。

 

示例 1：

输入：words = ["time", "me", "bell"]
输出：10
解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。
words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.08 没思路，直奔题解

# discard() 方法用于移除指定的集合元素。
# 该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
# 方法1, 存储后缀
from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)


# 方法2，字典树
# 一步一步来，首先是能看懂的版本
class Node(object):
    def __init__(self):
        self.children={}
class Solution2:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #需要去重，否则在之后计算“叶子高度”的时候会重复计算
        trie=Node() #这是字典树的根
        nodes=[] #这里保存着每个word对应的最后一个节点，比如对于单词time，它保存字母t对应的节点（因为是从后往前找的）
        for word in words:
            now=trie
            for w in reversed(word):
                if w in now.children:
                    now=now.children[w]
                else:
                    now.children[w]=Node()
                    now=now.children[w]
            nodes.append(now)
        ans=0
        for w,c in zip(words,nodes):
            if len(c.children)==0: #没有children，意味着这个节点是个叶子，nodes保存着每个word对应的最后一个节点，当它是一个叶子时，我们就该累加这个word的长度+1，这就是为什么我们在最开始要去重
                ans+=len(w)+1
        return ans

# 把node转为字典
class Solution3:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #需要去重，否则在之后计算“叶子高度”的时候会重复计算
        trie={} #这是字典树的根
        nodes=[] #这里保存着每个word对应的最后一个节点，比如对于单词time，它保存字母t对应的节点（因为是从后往前找的）
        for word in words:
            now=trie
            for w in reversed(word):
                if w in now:
                    now=now[w]
                else:
                    now[w]={}
                    now=now[w]
            nodes.append(now)
        ans=0
        for w,c in zip(words,nodes):
            if len(c)==0: #一个空字典，意味着这个节点是个叶子
                ans+=len(w)+1
        return ans


from functools import reduce
import collections
class Solution4:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

# 这道题有点意思，字典树挺有挑战的