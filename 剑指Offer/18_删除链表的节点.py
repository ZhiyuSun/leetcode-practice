"""

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 2021.04.23 我居然做出来了，不可思议
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                return head
            cur = cur.next

        return head

# 2021.04.23 K神的解法更清晰
class Solution1:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: pre.next = cur.next
        return head

# 2021.04.23 挑战下自己，加prev节点的解法
class Solution2:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        prev, cur = head, head.next
        while cur:
            if cur.val == val:
                prev.next = cur.next
                return head
            prev, cur = cur, cur.next
            