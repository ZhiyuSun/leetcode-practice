"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

例如，从根到叶子节点路径 1->2->3 代表数字 123。

计算从根到叶子节点生成的所有数字之和。

说明: 叶子节点是指没有子节点的节点。

示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 2020.10.29 BFS没有放弃我，干得漂亮
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [([root.val], root)]
        res = 0
        while queue:
            cur_list, node = queue.pop()
            if not node.left and not node.right:
                res += int("".join([str(item) for item in cur_list]))
            else:
                if node.left:
                    queue.append((cur_list + [node.left.val], node.left)) 
                if node.right:
                    queue.append((cur_list + [node.right.val], node.right))

        return res


# 官方解答，广度优先
import collections
class Solution1:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        total = 0
        nodeQueue = collections.deque([root])
        numQueue = collections.deque([root.val])
        
        while nodeQueue:
            node = nodeQueue.popleft()
            num = numQueue.popleft()
            left, right = node.left, node.right
            if not left and not right:
                total += num
            else:
                if left:
                    nodeQueue.append(left)
                    numQueue.append(num * 10 + left.val)
                if right:
                    nodeQueue.append(right)
                    numQueue.append(num * 10 + right.val)

        return total


# 官方解答，深度优先
class Solution2:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)

# 2021.07.07 我的广度优先，差点做不出来
class Solution3:
    def sumNumbers(self, root: TreeNode) -> int:
        queue = [(root, str(root.val))]
        res = 0
        while queue:
            node, val = queue.pop(0)
            if not node.left and not node.right:
                res += int(val)
            if node.left:
                queue.append((node.left, val + str(node.left.val)))
            if node.right:
                queue.append((node.right, val + str(node.right.val)))
        return res

# 2021.07.07 重温下深度优先
class Solution4:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)