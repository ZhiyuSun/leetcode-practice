"""
给定一棵二叉搜索树，请找出其中第k大的节点。

"""

# 2021.04.23 一个中序遍历解决
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        res = inorder(root)
        return res[-k]


# 2021.04.23 K神解法，中序遍历的倒序是右——根——左
# 在递归时同步的减1
class Solution1:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res
