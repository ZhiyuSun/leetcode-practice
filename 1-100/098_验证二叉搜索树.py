"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 我写的方法，按中序遍历做的
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        def _dfs(root):
            if not root: return []
            return _dfs(root.left) + [root.val] + _dfs(root.right)
        res = _dfs(root)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]: return False
        return True

# 官方解法
class Solution1:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False


            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True


        return helper(root)


# 2021.03.10 我的方法，一开始递归没做出来，采用中序遍历的思路
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        def inorderTraversal(node):
            if not node: return []
            return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
        res = inorderTraversal(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]: return False
        return True

# 2021.03.10 正解，需要在递归的时候，记录最大值和最小值
# 这是一种更加pythonic的代码
class Solution3:
    def isValidBST(self, root):
        
        def BFS(root, left, right):
            if root is None:
                return True
            
            if left < root.val < right:
                return BFS(root.left, left, root.val) and BFS(root.right, root.val, right)
            else:
                return False

        return BFS(root, -float('inf'), float('inf'))

# 2021.03.10 用栈实现中序遍历
class Solution4:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


# 2021.03.16 牛啊牛啊，中序遍历的迭代手法我自己写出来了
class Solution5:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        prev = float('-inf')
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if node.val <= prev:
                    return False
                prev = node.val
                root = node.right
        return True

# 2021.03.20 递归迭代不分家
class Solution6:
    def isValidBST(self, root: TreeNode) -> bool:
        def _dfs(root, left, right):
            if not root: return True
            if left < root.val < right:
                return _dfs(root.left, left, root.val) and _dfs(root.right, root.val, right)
            else:
                return False
        return _dfs(root, float('-inf'), float('inf'))