#!/usr/bin/python
# -*- coding: utf-8 -*-

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.store.append(word)
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.store

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for word in self.store:
            if word.startswith(prefix):
                return True
        
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# 代码效率有待提高