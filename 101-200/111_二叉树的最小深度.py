"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

"""
# 我写的BFS
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        queue = [root]
        while queue:
            res += 1
            for _ in range(0, len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return res
        return res

# 我写的DFS
class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        def _dfs(node, res):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return res
            res += 1
            return min(_dfs(node.left, res), _dfs(node.right, res))
        return _dfs(root, 1)