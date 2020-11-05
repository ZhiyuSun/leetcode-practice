#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
            
# 2020.09.16 被曾经的自己惊艳了

# 2020.11.5 我真是个five，做了3遍了都不会
class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root