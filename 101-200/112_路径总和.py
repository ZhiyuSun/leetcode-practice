"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2020.09.30 回味了之前的做法，很巧妙
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right):
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)



# 2021.03.10 隔了一晚上，还是靠自己的能力做了出来，做不出来是要崩溃的
class Solution1:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, cur):
            if not node.left and not node.right:
                return True if cur == targetSum else False
            else:
                if node.left and node.right:
                    return dfs(node.left, cur + node.left.val) or dfs(node.right, cur + node.right.val)
                if node.left:
                    return dfs(node.left, cur + node.left.val)
                if node.right:
                    return dfs(node.right, cur + node.right.val)

        if not root: return False

        return dfs(root, root.val)