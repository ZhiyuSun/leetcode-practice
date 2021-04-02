"""
一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。

假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。

例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。

与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意:

起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
所有的目标基因序列必须是合法的。
假定起始基因序列与目标基因序列是不一样的。
示例 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

返回值: 1
示例 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

返回值: 2
示例 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

返回值: 3

"""
from typing import List

# 2020.08.11 模仿单词接龙写的双向BFS
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank: return -1
        front = {start}
        back = {end}
        dist = 0
        wordList = set(bank)
        word_len = len(start)
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in ['A', 'C', 'G', 'T']:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return -1


# 2021.03.21 自己写出来了
class Solution2:
    def minMutation(self, start, end, bank):
        queue = [(start, 0)]
        bank = set(bank)
        while queue:
            cur, count = queue.pop(0)
            if cur == end: return count
            for i in range(0, len(start)):
                for ch in ['A', 'C', 'G', 'T']:
                    new = cur[0:i] + ch + cur[i+1:]
                    if new in bank:
                        queue.append((new, count+1))
                        bank.remove(new)
        return -1


# 2021.03.31 学习DFS的解法
class Solution3:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }

        min_count = len(bank) + 1

        def dfs(current, count, current_bank):
            nonlocal min_count

            # terminator
            if count > min_count:
                return
            if current == end:
                if count < min_count:
                    min_count = count
                return
            if not current_bank:
                return

            # process
            for i, s in enumerate(current):
                for char in change_map[s]:
                    new = current[:i] + char + current[i + 1:]
                    if new not in current_bank:
                        continue
                    current_bank.remove(new)
                    # drill down
                    dfs(new, count + 1, current_bank)

                    # reverse state
                    current_bank.add(new)

        dfs(start, 0, bank)

        return min_count if min_count <= len(bank) else -1


# 2021.03.31 学习双向BFS的解法
class Solution4:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change_map[s]:
                        new = node[:i] + c + node[i + 1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1
