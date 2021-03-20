"""
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List
import collections
# 我的解法
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        result = []
        previous_layer = [root]
        while previous_layer:
            result.append([])
            current_layer = []
            for node in previous_layer:
                result[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        return result


class Solution1:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = collections.deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        return result

class Solution2:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []        

        result = []
        previous_layer = [root]

        while previous_layer:
            current_layer = []
            result.append([])
            for node in previous_layer:
                result[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        return result

# 2021.03.20 BFS
class Solution3:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue, res = [root], []
        while queue:
            size = len(queue)
            cur = []
            for _ in range(size):
                node = queue.pop(0)
                cur.append(node.val)
                for child in node.children:
                    queue.append(child) 
            res.append(cur)
        return res

# 2021.03.20 DFS
class Solution4:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []

        if root is not None:
            traverse_node(root, 0)
        return result
