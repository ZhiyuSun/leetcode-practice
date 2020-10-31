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

        def reverseN(head: ListNode, n: int) -> ListNode:
            if n == 1: return head
            last = reverseN(head.next, n-1)
            successor = head.next.next
            head.next.next = head
            head.next = successor
            return last

        if m == 1: return reverseN(head, n)
        
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head


# 2020.10.31 为什么别人的可以.
# 结果是栽在了低级错误，把变量和类型写反了
class Solution1:
    def reverseBetween(self, head, m, n):
        def reverseN(head,n):
            if n == 1:
                return head
            # 以 head.next 为起点，需要反转前 n - 1 个节点
            last = reverseN(head.next, n-1)
            successor = head.next.next 
            # 以head.next为开头的链表已经完成翻转，那么head.next.next正确指向后继节点
            head.next.next = head
            head.next = successor
            return last
        if m == 1:return reverseN(head,n)
        head.next = self.reverseBetween(head.next,m-1,n-1)
        return head