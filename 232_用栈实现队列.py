#!/usr/bin/python
# -*- coding: utf-8 -*-

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
