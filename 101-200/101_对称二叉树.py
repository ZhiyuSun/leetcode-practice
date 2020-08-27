"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 我的蹩脚方法
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def _get_result(node, flag):
            if not node:
                return [None]
            if flag == 'left':
                return [node.val] + _get_result(node.left, 'left') + _get_result(node.right, 'left')
            else:
                return [node.val] + _get_result(node.right, 'right') + _get_result(node.left, 'right')


        return _get_result(root, 'left') == _get_result(root, 'right')

# 递归
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        return check(root, root)

# 迭代
class Solution2:
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