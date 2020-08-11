"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

"""
# 我的笨方法
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node):
            if not node: return 0
            queue = [node]
            height = 0
            while queue:
                height += 1
                for i in range(len(queue)):
                    n = queue.pop(0)
                    if n.left: queue.append(n.left)
                    if n.right: queue.append(n.right)
            return height


        if not root: return 0
        res = 0
        queue = [root]
        while queue:
            n = queue.pop()
            res = max(res, height(n.left)+height(n.right))
            if n.left: queue.append(n.left)
            if n.right: queue.append(n.right)
        return res

# 覃超老师的方法
class Solution1:
    def __init__(self):
        self.max_depth = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def _max_depth(root):
            if not root: return 0
            l = _max_depth(root.left)
            r = _max_depth(root.right)
            d = l + r
            self.max_depth = max(self.max_depth, d)
            return max(l, r) + 1
        _max_depth(root)
        return self.max_depth

# 官方解答
class Solution2(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node: return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L+R+1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1


        depth(root)
        return self.ans - 1