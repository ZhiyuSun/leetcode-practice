"""
编写一个程序，找到两个单链表相交的起始节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 2020.11.15 我的解法，应该能行得通，但是超时了
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        curA = headA
        while curA:
            curB = headB
            while curB:
                if curA == curB:
                    return curA
                curB = curB.next
            curA = curA.next

        return None
            
# 这个算法有点浪漫

# 若相交，链表A： a+c, 链表B : b+c. a+c+b+c = b+c+a+c 。则会在公共处c起点相遇。若不相交，a +b = b+a 。因此相遇处是NULL
# 错的人迟早会走散，而对的人迟早会相逢！

# 看下题解
# 哈希法
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = set()
        cur1 = headA
        cur2 = headB
        while cur1:
            A.add(cur1)
            cur1 = cur1.next
        while cur2:
            if cur2 in A:
                return cur2
            cur2 = cur2.next
        return None

# 双指针
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1


# 2021.02.09 我的解法，一开始出错了，后来没辙加了个falg
class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA
        q = headB
        falg_A = True
        falg_B = True
        while p and q:
            if p == q:
                return p
            if p.next or not falg_A:
                p = p.next
            else:
                falg_A = False
                p = headB
            if q.next or not falg_B:
                q = q.next
            else:
                falg_B = False
                q = headA
        return None