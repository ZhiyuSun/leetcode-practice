"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2020.08.18 我自己摸索出来的解法，时间复杂度高
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_path(node):
            if not node: return 0
            return max(get_path(node.left), get_path(node.right)) + 1

        def is_balance(node):
            if not node: return True
            left = get_path(node.left)
            right = get_path(node.right)
            if left == right or left - right == 1 or right - left == 1:
                return True
            return False

        if not root: return True
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not is_balance(node): return False
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return True

# 官方解法，学到了，其实可以在递归的时候，结合着判断
class Solutiondfs:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# 官方解法，继续优化，自底向上
class Solutionzdxs:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
