"""
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verifying-an-alien-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2021.04.24 这题其实可以很简单，我想复杂了
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True

