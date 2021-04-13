"""
现有一种使用英语字母的火星语言，这门语言的字母顺序与英语顺序不同。

给你一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

字符串 s 字典顺序小于 字符串 t 有两种情况：

在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/alien-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
from typing import List

# 2021.04.13 直奔题解，是我这辈子不会做的题了
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(list)
        
        indig = {}
        for word in words:
            for w in word:
                indig[w] = 0
        
        n = len(indig)

        for i in range(len(words) - 1):
            j = i + 1
            if len(words[i]) > len(words[j]) and words[j] == words[i][:len(words[j])]:
                return ''
            for k in range(min(len(words[i]), len(words[j]))):
                if words[i][k] == words[j][k]:
                    continue
                elif words[j][k] not in graph[words[i][k]]:
                    graph[words[i][k]].append(words[j][k])
                    indig[words[j][k]] += 1
                    break
                elif words[j][k] in graph[words[i][k]]:
                    break

        q = collections.deque([word for word in indig.keys() if indig[word] == 0])

        result = ''
        print(indig)
        print(graph)
        while q:
            word = q.popleft()
            result += word
            for w in graph[word]:
                indig[w] -= 1
                if indig[w] == 0:
                    q.append(w)
        return result if len(result) == len(graph) else ''
