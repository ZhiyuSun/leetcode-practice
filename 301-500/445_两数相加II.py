"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 2021.03.04 脑子绕不过来，直奔题解
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans

# 2021.03.04 模仿练习
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        ans = None
        while s1 or s2 or carry:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            cur = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            node = ListNode(cur)
            node.next = ans
            ans = node
        return ans

# 2021.03.04 不如直接数字法
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1

        def listnode2num(node):  # 将链表转换为数字(int)
            res = 0
            while node:
                res = res * 10 + node.val
                node = node.next
            return res

        result = listnode2num(l1) + listnode2num(l2)
        dummy_node = ListNode(0)  # 创建dummynode
        start_node = dummy_node
        for i in str(result):  # 讲结果相加结果转换为字符，然后逐位取出
            dummy_node.next = ListNode(int(i))  # 将取出的字符逐位放入新建的链表
            dummy_node = dummy_node.next
        return start_node.next