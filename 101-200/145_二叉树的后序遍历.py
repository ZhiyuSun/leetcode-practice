"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
                
        return output[::-1]


class Solution3:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []   # 用来存储后序遍历节点的值
        stack = []  
        node = root
        while stack or node:
            while node:
                stack.append(node)  # 第一次入栈的是根节点
                #判断当前节点的左子树是否存在，若存在则持续左下行，若不存在就转向右子树
                node = node.left if node.left is not None else node.right
            #循环结束说明走到了叶子节点，没有左右子树了，该叶子节点即为当前栈顶元素，应该访问了
            node = stack.pop() # 取出栈顶元素进行访问
            res.append(node.val) # 将栈顶元素也即当前节点的值添加进res
            # （下面的stack[-1]是执行完上面那句取出栈顶元素后的栈顶元素）
            if stack and stack[-1].left == node: #若栈不为空且当前节点是栈顶元素的左节点
                node = stack[-1].right   ## 则转向遍历右节点
            else:
                node = None  # 没有左子树或右子树，强迫退栈
        return res

# 2021.03.17 二叉树的后续遍历
class Solution4:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        return res[::-1]

# 2021.03.20 新增递归法
class Solution5:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(node):
            if not node: return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        res = []
        postorder(root)
        return res

# 2021.03.20 递归法变体
class Solution6:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        res.extend(self.postorderTraversal(root.left))
        res.extend(self.postorderTraversal(root.right))
        res.extend([root.val])
        return res