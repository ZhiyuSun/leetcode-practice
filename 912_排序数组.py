#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for s in range(len(nums)-i-1):
                if nums[s] > nums[s+1]:
                    nums[s], nums[s+1] = nums[s+1], nums[s]
        return nums
    
    # 冒泡排序
    def bubble_sort(self,nums):
        # 我们将标志值 swapped 设为 True，以便循环能够执行至少一次
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    # 交换元素
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # 把标志值设为 True 以便我们能再次循环
                    swapped = True
        return nums

    # 选择排序
    def selection_sort(self, nums):
        # i 的值对应于已排序值的数量
        for i in range(len(nums)):
            # 我们假设未排序部分的第一项是最小的
            lowest_value_index = i
            # 这个循环用来迭代未排序的项
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[lowest_value_index]:
                    lowest_value_index = j
            # 将未排序元素的最小的值与第一个未排序的元素的值相交换
            nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        return nums

    def heapify(self, nums, heap_size, root_index):
        # 设最大元素索引为根节点索引
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # 如果根节点的左子节点是有效索引，并且元素大于当前最大元素，则更新最大元素
        if left_child < heap_size and nums[left_child] > nums[largest]:
            largest = left_child

        # 对根节点的右子节点执行相同的操作
        if right_child < heap_size and nums[right_child] > nums[largest]:
            largest = right_child

        # 如果最大的元素不再是根元素，则交换它们
        if largest != root_index:
            nums[root_index], nums[largest] = nums[largest], nums[root_index]
            # 调整堆以确保新的根节点元素是最大元素
            self.heapify(nums, heap_size, largest)

    def heap_sort(self, nums):
        n = len(nums)

        # 利用列表创建一个最大堆
        # range 的第二个参数表示我们将停在索引值为 -1 的元素之前，即列表中的第一个元素
        # range 的第三个参数表示我们朝反方向迭代
        # 将 i 的值减少1
        for i in range(n, -1, -1):
            self.heapify(nums, n, i)

        # 将最大堆的根元素移动到列表末尾
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        
        return nums

    # 快速排序分区有不同的方法，下面实现了 Hoare 的分区方案。Tony Hoare 还创建了快速排序算法。
    def partition(self, nums, low, high):
        # 我们选择中间元素作为基准值。
        # 有些实现方法选择第一个元素或最后一个元素作为基准值。 
        # 有时将中间元素或一个随机元素作为基准值。
        # 还有很多可以选择或创建的方法。
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # 如果 i 处的元素（在基准值左侧）大于 j 处的元素（在基准值右侧），则交换它们。
            nums[i], nums[j] = nums[j], nums[i]


    def quick_sort(self, nums):
        # 创建一个辅助函数来进行递归调用
        def _quick_sort(items, low, high):
            if low < high:
                # 这是基准元素后的索引，我们的列表在这里被拆分
                split_index = self.partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quicksort2(self, nums):    
        if len(nums) <= 1:        
            return nums    
        pivot = nums[len(nums) // 2]    
        left = [x for x in nums if x < pivot]    
        middle = [x for x in nums if x == pivot]    
        right = [x for x in nums if x > pivot]    
        return self.quicksort2(left) + middle + self.quicksort2(right)

s = Solution()
print s.bubble_sort([1,3,4,6,2,8,0])
print s.selection_sort([1,3,4,6,2,8,0])
print s.heap_sort([1,3,4,6,2,8,0])
print s.quicksort2([1,3,4,6,2,8,0])


