"""
设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

实现 MagicDictionary 类：

MagicDictionary() 初始化对象
void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-magic-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import collections

# 2021.04.13 这解法创意很棒
class MagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a!=b for a,b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])

# 这个any和zip太精彩了