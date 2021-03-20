from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res

# 2021.03.17 痛不欲生，还是不会
class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res


# 2021.03.20 已经能用迭代法做出前序遍历了
class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack = [], [root]
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res

# 2021.03.20 自己研发递归法
class Solution4:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(node):
            if not node: return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        res = []
        preorder(root)
        return res


# 2021.03.20 从另一种递归法中得到的灵感
class Solution5:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = [root.val]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res