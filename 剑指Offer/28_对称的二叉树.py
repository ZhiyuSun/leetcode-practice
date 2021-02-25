"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2021.02.23 我居然做出来了，不可思议
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def compare(l, r):
            if not l and not r: return True
            if not l or not r: return False
            return l.val == r.val and compare(l.left, r.right) and compare(l.right, r.left)           
        return compare(root.left, root.right)


# 2021.02.23 参考官方的做法
# 递归
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        return check(root, root)

# 2021.02.23 参考官方的做法
# 迭代
class Solution3:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            u = queue.pop(0)
            v = queue.pop(0)
            if not u and not v: continue
            if (not u or not v) or (u.val != v.val): return False
            queue.append(u.left)
            queue.append(v.right)
            queue.append(u.right)
            queue.append(v.left)
        return True