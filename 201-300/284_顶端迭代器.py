"""
给定一个迭代器类的接口，接口包含两个方法： next() 和 hasNext()。设计并实现一个支持 peek() 操作的顶端迭代器 -- 其本质就是把原本应由 next() 方法返回的元素 peek() 出来。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/peeking-iterator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

# 2021.04.26 直奔题解，这题没啥意思
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        #用列表存储迭代器的值
        self.nums = []
        #目前遍历到列表的索引值
        self.index = 0
        #首先遍历一遍迭代器，存储数据，以便返回peek()函数的值
        while iterator.hasNext():
            self.nums.append(iterator.next())
        #总的列表的元素个数，目的是为了hasNext()函数的判断
        self.lenth = len(self.nums)
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """

        return self.nums[self.index]
        
    def next(self):
        """
        :rtype: int
        """
        #保存当前值
        value = self.nums[self.index]
        #索引加1，目的为了返回下一次值
        self.index += 1
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        #索引值判断是否遍历完成
        return self.index < self.lenth
