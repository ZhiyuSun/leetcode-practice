"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2020.9.26 调试了三番五次，依靠自己的力量做出来了 
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def _dfs(node, cur, path):
            if not node.left and not node.right and cur == sum:
                res.append(path[:])
            if node.left:
                _dfs(node.left, cur+node.left.val, path + [node.left.val])
            if node.right:
                _dfs(node.right, cur+node.right.val, path + [node.right.val])
        if not root:
            return []
        res = []
        _dfs(root, root.val, [root.val])
        return res


# 2020.9.29 补充BFS的写法

class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        queue = [(sum-root.val, [root])]
        res = []
        while queue:
            left, cur = queue.pop(0)
            if left == 0 and not cur[-1].left and not cur[-1].right:
                res.append([item.val for item in cur])
            if cur[-1].left:
                queue.append((left-cur[-1].left.val, cur + [cur[-1].left]))
            if cur[-1].right:
                queue.append((left-cur[-1].right.val, cur + [cur[-1].right]))
        return res
            
# 2021.04.13 小试牛刀
class Solution3:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def _dfs(node, s, path):
            if not node.left and not node.right:
                if s == targetSum:
                    res.append(path[:])
                else:
                    return
            if node.left:
                _dfs(node.left, s+node.left.val, path + [node.left.val])
            if node.right:
                _dfs(node.right, s+node.right.val, path + [node.right.val])

        if not root: return []
        res = []
        _dfs(root, root.val, [root.val])
        return res

# 2021.04.13 官方解法，重点学一下回溯法
class Solution4:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        ret = list()
        path = list()
        
        def dfs(root: TreeNode, total: int):
            if not root:
                return
            path.append(root.val)
            total -= root.val
            if not root.left and not root.right and total == 0:
                ret.append(path[:])
            dfs(root.left, total)
            dfs(root.right, total)
            path.pop()
        
        dfs(root, total)
        return ret

