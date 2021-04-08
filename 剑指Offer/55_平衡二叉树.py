"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2021.04.08 我的做法，能做出来，但感觉不优雅
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        def get_depth(node):
            if not node: return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1
        if abs(get_depth(root.left)-get_depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

# 2021.04.08 民间大神解法，长度和平衡可以一起考虑，若不平衡则返回-1
class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

# 2021.04.08 我的解法的优化版
class Solution3:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
