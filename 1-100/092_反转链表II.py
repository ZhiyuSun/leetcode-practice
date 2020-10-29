"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 巧用递归，化整为零，绝了
# https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/bu-bu-chai-jie-ru-he-di-gui-di-fan-zhuan-lian-biao/
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        def reverseN(head: ListNode, int: n) -> ListNode:
            if n == 1: return head
            last = reverseN(head.next, n-1)
            successor = head.next.next
            head.next.next = head
            head.next = successor
            return last

        if m == 1: return reverseN(head, n)
        
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head