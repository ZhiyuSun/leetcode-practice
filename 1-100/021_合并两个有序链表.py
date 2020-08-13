#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 官方解答
# 递归的思路
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# 另一种思路
class Solution2:
    def mergeTwoLists(self, l1, l2):
        root = ListNode(None)
        cur = root
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            cur.next = node
            cur = node
        cur.next = l1 or l2
        return root.next

# 2020.08.13 我居然自己写出来了
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solutionself:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        p = res
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next
        if l1: res.next = l1
        if l2: res.next = l2
        return p.next
