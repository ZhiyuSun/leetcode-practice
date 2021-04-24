"""
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2021.04.24 我自己的做法，回溯
class Solution:
    def __init__(self):
        self.res = 0
    
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if not root: return 0
        def _dfs(node, dic):
            if not node.left and not node.right:
                count = 1
                for k, v in dic.items():
                    if v % 2 == 1:
                        count -= 1
                    if count < 0:
                        break
                if count >= 0:
                    self.res += 1
                return
            if node.left:
                dic[node.left.val] += 1
                _dfs(node.left, dic)
                dic[node.left.val] -= 1
            if node.right:
                dic[node.right.val] += 1
                _dfs(node.right, dic)
                dic[node.right.val] -= 1

        dic = collections.defaultdict(int)
        dic[root.val] += 1
        _dfs(root, dic)
        return self.res


# 2021.04.24 位运算的做法神了
class Solution1:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(record, root):
            if root:
                record ^= (1 << root.val)
                if not(root.left or root.right):
                    if bin(record).count("1") < 2:
                        self.ans += 1
                    return
                dfs(record, root.left)
                dfs(record, root.right)
            
        dfs(0, root)
        return self.ans