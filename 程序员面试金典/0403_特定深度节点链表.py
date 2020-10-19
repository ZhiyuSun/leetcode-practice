"""
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \ 
      2    3
     / \    \ 
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/list-of-depth-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2020.9.16 在一番挣扎后写了出来，需活用树和链表
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        res = []
        queue = [tree]
        while queue:
            head = ListNode(None)
            start = head
            for _ in range(len(queue)):
                cur = queue.pop(0)
                head.next = ListNode(cur.val)
                head = head.next
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(start.next)  
        return res


# 网上的其他解法，不太容易理解
class Solution1:
    def listOfDepth(self, root: TreeNode) -> List[ListNode]:
        ans = []
        def dfs(node, level):
            if not node: return None
            if len(ans) == level:
                ans.append(ListNode(node.val))
            else:
                head = ListNode(node.val)
                head.next = ans[level]
                ans[level] = head
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return ans
