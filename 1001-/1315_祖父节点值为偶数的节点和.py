"""
给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：

该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
如果不存在祖父节点值为偶数的节点，那么返回 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 2021.04.14 我的做法，轻轻松松
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    res += root.left.left.val
                if root.left.right:
                    res += root.left.right.val
            if root.right:
                if root.right.left:
                    res += root.right.left.val
                if root.right.right:
                    res += root.right.right.val
        return res + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)


# 2021.04.14 官方解法，BFS
class Solution1:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = collections.deque([root])
        ans = 0
        while len(q) > 0:
            node = q.popleft()
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        ans += node.left.left.val
                    if node.left.right:
                        ans += node.left.right.val
                if node.right:
                    if node.right.left:
                        ans += node.right.left.val
                    if node.right.right:
                        ans += node.right.right.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans

# 2021.04.14 民间解法 DFS
class Solution2:
    def __init__(self):
        self.res=0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def recursion(root:TreeNode,lev2:int,lev1:int):
            if root:
                recursion(root.left,lev1,root.val)
                recursion(root.right,lev1,root.val)

                if lev2%2==0 and lev2!=0:
                    self.res +=root.val
                    
        recursion(root,0,0)
        return self.res
