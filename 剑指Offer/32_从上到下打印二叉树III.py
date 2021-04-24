"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
"""

# Definition for a binary tree node.
import collections
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 2021.04.24 相当熟练
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        q = collections.deque()
        q.append(root)
        order = False
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if order:
                temp.reverse()
            order = not order
            res.append(temp)
        return res


# 2021.04.24 K神解法，运用res来判断奇偶，真的秀
class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp[::-1] if len(res) % 2 else tmp)
        return res