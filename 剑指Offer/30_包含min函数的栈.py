"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""

# 2021.04.24 我的解法
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if self.stack2:
            min_value = min(self.stack2[-1], x)
        else:
            min_value = x
        self.stack2.append(min_value)

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()


    def top(self) -> int:
        return self.stack1[-1]


    def min(self) -> int:
        return self.stack2[-1]

# 2021.04.24 K神解法
class MinStack1:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]

