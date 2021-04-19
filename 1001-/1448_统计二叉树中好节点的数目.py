"""
给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。

「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2021.04.19 我的递归能力还是可以的
class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return self.res

        def _dfs(node, max_value):
            if node.val >= max_value:
                self.res += 1
            max_value = max(node.val, max_value)
            if node.left:
                _dfs(node.left, max_value)
            if node.right:
                _dfs(node.right, max_value)

        _dfs(root, float('-inf'))
        return self.res