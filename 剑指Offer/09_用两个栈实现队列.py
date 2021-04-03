"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.04.02 我的解法
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(value)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def deleteHead(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


# 2021.04.03 参考大神的解法，一个负责进，一个负责出
class CQueue2:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if not self.stack_out:
            if not self.stack_in: # 都为空
                return -1
            else: # 把in栈中的东西全部倒入out栈中
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out.pop()