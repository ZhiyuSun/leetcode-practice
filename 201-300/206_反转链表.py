"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

# 2021.02.22 两种方法，递归法和遍历法
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

# 2021.03.18 自己还是不会，抄了一遍题解，需要注意
class Solution4:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev