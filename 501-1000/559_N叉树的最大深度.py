"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 我的解法
class Solution:
    def __init__(self):
        self.max_hight = 0

    def maxDepth(self, root: 'Node') -> int:
        def _dfs(root, height):
            if not root: return
            height += 1
            self.max_hight = max(height, self.max_hight)
            for node in root.children:
                _dfs(node, height)
            
        _dfs(root, 0)
        return self.max_hight


# 官方解法——递归

class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None: 
            return 0 
        elif root.children == []:
            return 1
        else: 
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1 

# 官方解法2——迭代
class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """ 
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))
                
        return depth
