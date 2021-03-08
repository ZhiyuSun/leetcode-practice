"""
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack1.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack1[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if self.stack1 else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# 慕课网的解答
# 不一定每次都要重新倒元素
class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self, val):
        return self.items.append(val)
    
    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MyQueue1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        return self.s2.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        return self.s2.top()
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.s1.empty() and self.s2.empty()


def test():
    a = MyQueue1()
    a.push(1)
    a.push(2)
    a.peek()
    a.pop()
    a.empty()

test()


# 2021.03.05 巧妙运用两个栈，减少时间复杂度
class MyQueue2:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2
