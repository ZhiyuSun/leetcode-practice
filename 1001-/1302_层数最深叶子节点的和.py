"""
给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 
"""
import collections


# 2021.04.18 这只能算简单题吧

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append(root)
        res = 0
        while queue:
            res = 0
            for i in range(len(queue)):
                node = queue.popleft()
                res += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return res


# 2021.04.18 官方解法赏析，DFS
class Solution1:
    def __init__(self):
        self.maxdep = -1
        self.total = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(node, dep):
            if not node:
                return
            if dep > self.maxdep:
                self.maxdep, self.total = dep, node.val
            elif dep == self.maxdep:
                self.total += node.val
            dfs(node.left, dep + 1)
            dfs(node.right, dep + 1)
        
        dfs(root, 0)
        return self.total

# 2021.04.18 官方解法赏析，BFS
class Solution2:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = collections.deque([(root, 0)])
        maxdep, total = -1, 0
        while len(q) > 0:
            node, dep = q.pop()
            if dep > maxdep:
                maxdep, total = dep, node.val
            elif dep == maxdep:
                total += node.val
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))
        return total
