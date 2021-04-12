"""
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
"""

# 2021.04.12 简单题，不费吹灰之力
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        target = count // 2
        for _ in range(target):
            head = head.next
        return head

# 2021.04.12 官方解法，数组法
class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

# 2021.04.12 官方解法，单指针法
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        k, cur = 0, head
        while k < n // 2:
            k += 1
            cur = cur.next
        return cur

# 2021.04.12 官方解法，快慢指针法
class Solution3:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
