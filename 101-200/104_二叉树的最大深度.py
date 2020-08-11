"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 我的解法
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        def _dfs(node, height):
            if not node:
                return height
            if not node.left and not node.right:
                return height
            else:
                height += 1
                return max(_dfs(node.left, height), _dfs(node.right, height))
        return _dfs(root, 1)

# 官方解法DFS
class Solution1:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

# 广度优先

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res += 1
        return res

