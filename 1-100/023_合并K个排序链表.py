#!/usr/bin/python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heapify, heappop

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 读取所有的节点值
        h = []
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        # 构造一个最小堆
        heapify(h)

        if not h:
            return None
        # 构造链表
        root = ListNode(heappop(h))
        curnode = root
        while h:
            nextnode = ListNode(heappop(h))
            curnode.next = nextnode
            curnode = nextnode
        return root

# 官方解答
# 用普通排序就行，没必要用堆排序
class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
