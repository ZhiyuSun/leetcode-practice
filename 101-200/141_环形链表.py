"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        p = head
        q = head.next
        while p != q:
            if not q or not q.next: return False
            p = p.next
            q = q.next.next
        return True

# 220.09.01
# 哈希表的方法
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        visited = set()
        node = head
        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False


# 2021.01.21 环形链表
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        node_set = set()
        while head:
            if head in node_set:
                return True
            else:
                node_set.add(head)
            head = head.next
        return False

# 双指针
class Solution3:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        p = head
        q = head.next
        while p != q:
            if not q or not q.next: return False
            p = p.next
            q = q.next.next

        return True


# 2021.02.09 面试倒计时
# 我的解法，哈希表法
class Solution4:
    def hasCycle(self, head: ListNode) -> bool:
        node_set= set()
        while head:
            if head in node_set:
                return True
            else:
                node_set.add(head)
            head = head.next
        return False


# 我的解法，双指针法，类似追及问题
class Solution5:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        p = head
        q = head.next
        while p and q:
            if p == q: return True
            p = p.next
            q = q.next
            if q:
                q = q.next
            else:
                return False
        return False

# 参考之前的解法的双指针的优化版
class Solution6:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False
        p = head
        q = head.next
        while p != q:
            if not q or not q.next: return False
            p = p.next
            q = q.next.next
        return True