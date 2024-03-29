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

# 2021.03.11 自己写出来了，这道题给了我很多自信
class Solution3:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def compare_nodes(left, right):
            if not left and not right: return True
            if not left or not right: return False
            return left.val == right.val and compare_nodes(left.left, right.right) and compare_nodes(left.right, right.left)

        return compare_nodes(root.left, root.right)

# 这道题也可以用BFS，不过要注意入队列的顺序

# 2021.06.13 恢复很快
class Solution4:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def compare(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and compare(node1.left, node2.right) and compare(node1.right, node2.left)
        return compare(root.left, root.right)