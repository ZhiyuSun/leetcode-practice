"""

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2021.04.26 链表的题目真容易让人凌乱啊，但还是做出来了
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        if count == n:
            return head.next
        cur = head
        for i in range(count-n-1):
            cur = cur.next
        n = cur.next
        if n:
            cur.next = n.next
        else:
            cur.next = None
        return head


# 2021.04.26 我上面的优化版，尾结点其实是必有的
class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return None
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        if count == n:
            return head.next
        cur = head
        for i in range(count-n-1):
            cur = cur.next
        cur.next = cur.next.next
        return head


# 2021.04.26 哑结点的方法很有用
class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next