"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2020.9.2 直奔题解，但感觉没发挥出二叉搜索树的优势
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dicts = {}

        ##使用DFS来整一遍
        def dfs(root):
            if not root:
                return 
            if root.val not in dicts:
                dicts[root.val] = 1
            else:
                dicts[root.val]+=1
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        maxVal = max(dicts.values())
        ans = []
        for item,val in dicts.items():
            if val>=maxVal:
                ans.append(item)
        return ans


# 2021.04.25 在中序遍历的过程中找结果
class Solution1:
    def findMode(self, root: TreeNode) -> List[int]:
        ans=[]
        most=0
        last=None
        cnt=0

        def inorder(node):
            if not node: return 
            nonlocal ans,most,last,cnt
            if node.left: inorder(node.left)
            if node.val==last:
                cnt+=1
            else: cnt=1
            if cnt==most: ans.append(node.val)
            elif cnt>most:
                most=cnt
                ans=[node.val]
            last=node.val
            if node.right: inorder(node.right)

        inorder(root)
        return ans