"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true

说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
"""

class Node:
    def __init__(self, val=None, next=[], isEnd=False):
        self.val = val
        self.next = {i.val: i for i in next}
        self.isEnd = isEnd


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.node
        for i in word:
            if i not in tmp.next:
                tmp.next[i] = Node(i)
            tmp = tmp.next[i]
        tmp.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.node
        for i in word[:-1]:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        if word[-1] not in tmp.next:
            return False
        if tmp.next[word[-1]].isEnd:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.node
        for i in prefix:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# 2021.03.29 温习一遍


# 2021.04.18 优化了一遍前缀树
class Trie2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.node
        for i in word:
            if i not in tmp.next:
                tmp.next[i] = Node(i)
            tmp = tmp.next[i]
        tmp.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.node
        for i in word:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        return tmp.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.node
        for i in prefix:
            if i not in tmp.next:
                return False
            tmp = tmp.next[i]
        return True


# 2021.04.18 我的解法
class Trie3:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        dic = self.dic
        for i in word:
            if i in dic:
                dic = dic[i]
            else:
                dic[i] = {}
                dic = dic[i]
        dic['0'] = 0

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        dic = self.dic
        for i in word:
            if i in dic:
                dic = dic[i]
            else:
                return False
        return '0' in dic

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        dic = self.dic
        for i in prefix:
            if i in dic:
                dic = dic[i]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# 2021.04.18 官方解法，也可以用数组来表示
class Trie4:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
