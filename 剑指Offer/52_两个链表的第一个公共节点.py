"""
输入两个链表，找出它们的第一个公共节点。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 2021.04.23 我也太强了
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        while True:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
# 2021.04.23 官方解法赏析
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
