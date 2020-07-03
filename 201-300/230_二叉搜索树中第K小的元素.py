#!/usr/bin/python
# -*- coding: utf-8 -*-

# 中序遍历，看了答案后我才知道的，我实在是太菜了
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
	"""
	:type root: TreeNode
	:type k: int
	:rtype: int
	"""
	res = []
	self.visitNode(root, res)
	return res[k - 1]

    # 中序遍历
    def visitNode(self, root, res):
	if root is None:
	    return
	self.visitNode(root.left, res)
	res.append(root.val)
	self.visitNode(root.right, res)
