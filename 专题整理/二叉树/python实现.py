class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
from collections import deque

# 94. 二叉树的中序遍历
class Solution94:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        def inorder(node):
            if not node: return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res


# 144. 二叉树的前序遍历
class Solution144:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        def preorder(node):
            if not node: return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        res = []
        preorder(root)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res

# 145. 二叉树的后序遍历
class Solution145:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        def postorder(node):
            if not node: return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        res = []
        postorder(root)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
                
        return output[::-1]

# 102. 二叉树的层序遍历
class Solution102:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = deque([root])
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res

# 112. 路径总和
class Solution112:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right):
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

# 104. 二叉树的最大深度
class Solution104:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 111. 二叉树的最小深度
class Solution111:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# 101. 对称二叉树
class Solution101:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        return check(root, root)

    def isSymmetric1(self, root: TreeNode) -> bool:
        queue = [root, root]
        while queue:
            u = queue.pop(0)
            v = queue.pop(0)
            if not u and not v: continue
            if (not u or not v) or (u.val != v.val): return False
            queue.append(u.left)
            queue.append(v.right)
            queue.append(u.right)
            queue.append(v.left)
        return True


# 236. 二叉树的最近公共祖先
class Solution236:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root

# 105. 从前序与中序遍历序列构造二叉树
class Solution105:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = preorder[in_left]
            root = TreeNode(val)

            index = idx_map[val]
 
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root
        
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)

# 226. 翻转二叉树
class Solution226:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# 98. 验证二叉搜索树
class Solution98:
    def isValidBST(self, root: TreeNode) -> bool:
        def _dfs(root, left, right):
            if not root: return True
            if left < root.val < right:
                return _dfs(root.left, left, root.val) and _dfs(root.right, root.val, right)
            else:
                return False
        return _dfs(root, float('-inf'), float('inf'))