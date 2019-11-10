#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 我的答案，太丑陋了吧
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root or root.val is None:
            return []
        level = [root]
        result = []
        while level:
            level_result = [i.val for i in level if i]
            result.append(level_result)
            next_level = []
            for i in level:
                if i:
                    if i.left:
                        next_level.append(i.left)
                    if i.right:
                        next_level.append(i.right)
            level = next_level
        return result

# 民间写法
class Solution1:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        cur_nodes = [root]
        next_nodes = []
        res.append([i.val for i in cur_nodes])
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if next_nodes:
                res.append(
                    [i.val for i in next_nodes]
                )
            cur_nodes = next_nodes
            next_nodes = []
        return res
 

#我的改进版
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        result = []
        while level:
            level_result = [i.val for i in level]
            result.append(level_result)
            next_level = []
            for i in level:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            level = next_level
        return result
                