"""
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# 2021.03.09 掌握基本的层序遍历，即可得到思路
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = [root]
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i < size-1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


# 2021.03.09 参考了民间大神的解法，这个清楚多了
class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        first = root
        while first:
            head = None
            tail = Node()
            cur = first
            while cur:
                if cur.left:
                    if not head:
                        head = cur.left
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    if not head:
                        head = cur.right
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            first = head
        return root