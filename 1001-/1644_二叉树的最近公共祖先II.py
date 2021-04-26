"""
给定一棵二叉树的根节点 root，返回给定节点 p 和 q 的最近公共祖先（LCA）节点。如果 p 或 q 之一不存在于该二叉树中，返回 null。树中的每个节点值都是互不相同的。

根据维基百科中对最近公共祖先节点的定义：“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是后代节点中既包括 p 又包括 q 的最深节点（我们允许一个节点为自身的一个后代节点）”。一个节点 x 的后代节点是节点 x 到某一叶节点间的路径中的节点 y。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2021.04.26 多一个判断节点是否在二叉树中的步骤
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #先判断p和q是不是都在树中
        self.flag_p, self.flag_q = False, False
        self.dfs(root, p, q)
        if not (self.flag_p == True and self.flag_q == True):
            return None
        
        return self.dfs_LRN(root, p, q)
    
    def dfs(self, root, p, q) -> None:    #判断p和q都在不在树中
        if root == p:
            self.flag_p = True
        if root == q:
            self.flag_q = True
        if root.left:
            self.dfs(root.left, p, q)
        if root.right:
            self.dfs(root.right, p, q)
    
    def dfs_LRN(self, root, p, q) -> TreeNode:  #后序遍历，找LCA
        if root==None or root==p or root==q:
            return root
        L = self.dfs_LRN(root.left, p, q)
        R = self.dfs_LRN(root.right, p, q)
        if L and R:
            return root
        elif L and R==None:
            return L
        elif L==None and R:
            return R
        else:
            return None
