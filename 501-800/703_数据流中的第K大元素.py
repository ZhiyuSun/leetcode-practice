"""
设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest 类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
 

示例：

输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.03.25 我已经能灵活运用heapq模块了

import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        arr = nums[0:k]
        heapq.heapify(arr)
        for i in nums[k:]:
            if i > arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr, i)
        self.arr = arr
        self.k = k

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            heapq.heappush(self.arr, val)
            return self.arr[0]
        if val < self.arr[0]: 
            return self.arr[0]
        else:
            heapq.heappop(self.arr)
            heapq.heappush(self.arr, val)
            return self.arr[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# 2021.03.25 负明雪烛的算法
class KthLargest2:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.que = nums
        heapq.heapify(self.que)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.que, val)
        while len(self.que) > self.k:
            heapq.heappop(self.que)
        return self.que[0]

# 2021.03.25 其他大神的解法
class KthLargest3:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap,num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# 2021.03.25 民间大神，手写实现
class Heap:
    def __init__(self,desc=False):
        """
        初始化，默认创建一个小顶堆
        """
        self.heap = []
        self.desc = desc
    
    @property
    def size(self):
        return len(self.heap)
    
    def top(self):
        if self.size:
            return self.heap[0]
        return None
    
    def push(self,item):
        """
        添加元素
        第一步，把元素加入到数组末尾
        第二步，把末尾元素向上调整
        """
        self.heap.append(item)
        self._sift_up(self.size-1)
    
    def pop(self):
        """
        弹出堆顶
        第一步，记录堆顶元素的值
        第二步，交换堆顶元素与末尾元素
        第三步，删除数组末尾元素
        第四步，新的堆顶元素向下调整
        第五步，返回答案
        """
        item = self.heap[0]
        self._swap(0,self.size-1)
        self.heap.pop()
        self._sift_down(0)
        return item
    
    def _smaller(self,lhs,rhs):
        return lhs > rhs if self.desc else lhs < rhs
    
    def _sift_up(self,index):
        """
        向上调整
        如果父节点和当前节点满足交换的关系
        （对于小顶堆是父节点元素更大，对于大顶堆是父节点更小），
        则持续将当前节点向上调整
        """
        while index:
            parent = (index-1) // 2
            
            if self._smaller(self.heap[parent],self.heap[index]):
                break
                
            self._swap(parent,index)
            index = parent
    
    def _sift_down(self,index):
        """
        向下调整
        如果子节点和当前节点满足交换的关系
        （对于小顶堆是子节点元素更小，对于大顶堆是子节点更大），
        则持续将当前节点向下调整
        """
        # 若存在子节点
        while index*2+1 < self.size:
            smallest = index
            left = index*2+1
            right = index*2+2
            
            if self._smaller(self.heap[left],self.heap[smallest]):
                smallest = left
                
            if right < self.size and self._smaller(self.heap[right],self.heap[smallest]):
                smallest = right
                
            if smallest == index:
                break
            
            self._swap(index,smallest)
            index = smallest
    
    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

class KthLargest4:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap()
        self.k = k
        for num in nums:
            self.heap.push(num)
            if self.heap.size > k:
                self.heap.pop()


    def add(self, val: int) -> int:
        self.heap.push(val)
        if self.heap.size > self.k:
            self.heap.pop()
        return self.heap.top()
