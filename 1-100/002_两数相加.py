"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2021.02.21 摸爬滚打做出来了
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        l3 = head
        m = 0
        while l1 or l2:
            if l1:
                l = l1.val
                l1 = l1.next
            else:
                l = 0
            if l2:
                r = l2.val
                l2 = l2.next
            else:
                r = 0
            s = l + r + m
            l3.next = ListNode(s % 10)
            l3 = l3.next
            m = s // 10
        if m > 0:
            l3.next = ListNode(m)
        return head.next

# 2021.02.21 参考的别人的Python解法
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry

            if l1: l1, val = l1.next, l1.val + val
            if l2: l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)
        
        return head.next