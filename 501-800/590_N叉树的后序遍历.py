"""
给定一个 N 叉树，返回其节点值的 后序遍历 。

N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
"""

# 2021.03.18 借鉴二叉树
from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack, res = [root], []
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            for i in tmp.children:
                stack.append(i)
        return res[::-1]


# 2021.03.18 递归法
class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        result = []
        for child_root in root.children:
            result.extend(self.postorder(child_root))
        result.append(root.val)
        return result
