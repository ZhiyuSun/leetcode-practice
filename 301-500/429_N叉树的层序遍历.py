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
