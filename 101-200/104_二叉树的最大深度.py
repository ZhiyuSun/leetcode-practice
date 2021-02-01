"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 我的解法
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        def _dfs(node, height):
            if not node:
                return height
            if not node.left and not node.right:
                return height
            else:
                height += 1
                return max(_dfs(node.left, height), _dfs(node.right, height))
        return _dfs(root, 1)

# 官方解法DFS
class Solution1:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

# 广度优先

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res += 1
        return res


# 2021.01.07 再战
class Solution3:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [[root]]
        ans = 0
        while queue:
            ans+=1
            cur_level = queue.pop()
            nex_level = []
            for i in cur_level:
                if i.left:
                    nex_level.append(i.left)
                if i.right:
                    nex_level.append(i.right)
            if nex_level:
                queue.append(nex_level)
        return ans

# 广度优先，没有之前的做法优雅，惭愧惭愧


# 复杂度分析：
# DFS
# 时间复杂度：O(n)O(n)，其中 nn 为二叉树节点的个数。每个节点在递归中只被遍历一次。
# 空间复杂度：O(\textit{height})O(height)，其中 \textit{height}height 表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。

# BFS
# 时间复杂度：O(n)O(n)，其中 nn 为二叉树的节点个数。与方法一同样的分析，每个节点只会被访问一次。
# 空间复杂度：此方法空间的消耗取决于队列存储的元素数量，其在最坏情况下会达到 O(n)O(n)。


# 2021.01.28 递归法
class Solution4:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1