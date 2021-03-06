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
                

class Solution3(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res = []
		queue = [root]
		while queue:
			# 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
			size = len(queue)
			tmp = []
			# 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
			# 如果节点的左/右子树不为空，也放入队列中
			for _ in range(size):
				r = queue.pop(0)
				tmp.append(r.val)
				if r.left:
					queue.append(r.left)
				if r.right:
					queue.append(r.right)
			# 将临时list加入最终返回结果中
			res.append(tmp)
		return res
