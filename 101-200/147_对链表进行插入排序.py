"""
插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insertion-sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.08.19 又是直奔题解的一天
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cur, nxt = head, head.next
        dummy = ListNode(float('-inf'))
        dummy.next = head
        while nxt:
            if nxt.val >= cur.val:
                cur = nxt
                nxt = nxt.next
            else:
                cur.next = nxt.next
                pre1, pre2 = dummy, dummy.next
                while nxt.val > pre2.val:
                    pre1 = pre2
                    pre2 = pre2.next
                pre1.next = nxt
                nxt.next = pre2
                nxt = cur.next
        return dummy.next

# 2021.02.22 还是不会
class Solution1:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next
        
        return dummyHead.next
