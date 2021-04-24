"""
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2021.04.24 重在参与，这题完全不会
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return [float("inf"), 0, 0]
            
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]
        
        a, b, c = dfs(root)
        return b
