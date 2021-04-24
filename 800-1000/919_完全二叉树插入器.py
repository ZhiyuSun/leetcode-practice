"""
完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：

CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
CBTInserter.get_root() 将返回树的头节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/complete-binary-tree-inserter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2021.04.24 对这道题不明所以
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v: int) -> int:
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self) -> TreeNode:
        return self.root
