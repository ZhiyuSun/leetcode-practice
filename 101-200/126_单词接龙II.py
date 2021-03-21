"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from collections import defaultdict
from typing import List
from collections import deque
import string


# 2021.03.21 直奔题解，这道题是真难啊
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        # key：字符串，value：广度优先遍历过程中 key 的后继结点列表
        found = self.__bidirectional_bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bidirectional_bfs(self, beginWord, endWord, word_set, successors):
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)

        begin_visited = set()
        begin_visited.add(beginWord)

        end_visited = set()
        end_visited.add(endWord)

        found = False
        forward = True
        word_len = len(beginWord)
        while begin_visited:
            if len(begin_visited) > len(end_visited):
                begin_visited, end_visited = end_visited, begin_visited
                forward = not forward

            next_level_visited = set()
            for current_word in begin_visited:
                word_list = list(current_word)
                for j in range(word_len):
                    origin_char = word_list[j]
                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word in end_visited:
                                found = True
                                # 在另一侧找到单词以后，还需把这一层关系添加到「后继结点列表」
                                self.__add_to_successors(successors, forward, current_word, next_word)
                            if next_word not in visited:
                                next_level_visited.add(next_word)
                                self.__add_to_successors(successors, forward, current_word, next_word)
                    word_list[j] = origin_char
            begin_visited = next_level_visited
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited |= next_level_visited
            if found:
                break
        return found

    def __add_to_successors(self, successors, forward, current_word, next_word):
        if forward:
            successors[current_word].add(next_word)
        else:
            successors[next_word].add(current_word)

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()
