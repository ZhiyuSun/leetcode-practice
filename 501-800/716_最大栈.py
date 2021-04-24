"""
设计一个最大栈数据结构，既支持栈操作，又支持查找栈中最大元素。

实现 MaxStack 类：

MaxStack() 初始化栈对象
void push(int x) 将元素 x 压入栈中。
int pop() 移除栈顶元素并返回这个元素。
int top() 返回栈顶元素，无需移除。
int peekMax() 检索并返回栈中最大元素，无需移除。
int popMax() 检索并返回栈中最大元素，并将其移除。如果有多个最大元素，只要移除 最靠近栈顶 的那个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.24 直奔题解，删除最大元素有点复杂
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_stk = []
        self.max_stk = []

    def push(self, x: int) -> None:
        if self.max_stk == [] or x > self.max_stk[-1]:
            self.max_stk.append(x)
        else:
            self.max_stk.append(self.max_stk[-1])
        
        self.num_stk.append(x)

    def pop(self) -> int:
        self.max_stk.pop(-1)
        return self.num_stk.pop(-1)

    def top(self) -> int:
        return self.num_stk[-1]

    def peekMax(self) -> int:
        return self.max_stk[-1]

    def popMax(self) -> int:
        cur_max = self.max_stk[-1]

        tmp = []
        while self.num_stk[-1] != cur_max:
            tmp.append(self.pop())          #2个栈一起弹

        self.pop()
        
        while tmp:
            self.push(tmp.pop(-1))          #2个栈一起压
        return cur_max

# 2021.04.24 还有很多奇怪的解法，比如双向链表+平衡树，就不学了
