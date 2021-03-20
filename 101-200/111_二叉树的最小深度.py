"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.

"""
# 我写的BFS
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        queue = [root]
        while queue:
            res += 1
            for _ in range(0, len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return res
        return res

# 我写的DFS
class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        def _dfs(node, res):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return res
            res += 1
            return min(_dfs(node.left, res), _dfs(node.right, res))
        return _dfs(root, 1)


# 2021.01.07 误打误撞  DFS
class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1


# 2021.01.07 BFS 成神了
class Solution3:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [[root]]
        ans = 1
        while queue:
            cur_level = queue.pop()
            nex_level = []
            for i in cur_level:
                if not i.left and not i.right:
                    return ans
                if i.left:
                    nex_level.append(i.left)
                if i.right:
                    nex_level.append(i.right)
            if nex_level:
                queue.append(nex_level)
            ans += 1
        return ans



# 复杂度分析
# DFS
# 时间复杂度：O(N)O(N)，其中 NN 是树的节点数。对每个节点访问一次。
# 空间复杂度：O(N)O(N)，其中 NN 是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数。

# BFS
# 时间复杂度：O(N)O(N)，其中 NN 是树的节点数。对每个节点访问一次。
# 空间复杂度：O(N)O(N)，其中 NN 是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数。


# 2021.02.02 再战，稍微迟疑了一会儿，运用递归的思路还是能写出来
class Solution4:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# 2021.03.20 佩服自己，对面试有信心了
class Solution5:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1