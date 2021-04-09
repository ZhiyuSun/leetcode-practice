"""
给你一个整数数组 nums，请你将该数组升序排列。

 

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
from typing import List

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

    # 插入排序
    def insert_sort(self, nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                temp = nums[i]
                index = i
                for j in range(i-1, -1, -1):
                    if nums[j] > temp:
                        nums[j+1] = nums[j]
                        index = j
                    else:
                        break
                nums[index] = temp
        return nums

    # 归并排序
    def merge_sort(self, nums):
        self.do_merge_sort(nums, 0, len(nums) - 1)
        return nums

    def do_merge_sort(self, nums, l, r):
        if l == r: return
        mid = (l+r) // 2
        self.do_merge_sort(nums, l, mid)
        self.do_merge_sort(nums, mid+1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j<=r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l:r+1] = tmp

    # 堆排序
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
        else:
            pivot = nums[0]
            less = [x for x in nums[1:] if x < pivot]
            greater = [x for x in nums[1:] if x >= pivot]
            return self.quicksort2(less) + [pivot] + self.quicksort2(greater)

    def randomized_partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def quick_sort3(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums


    # def max_heapify(self, heap, root, heap_len):
    #     p = root
    #     while p * 2 + 1 < heap_len:
    #         l, r = p * 2 + 1, p * 2 + 2
    #         if heap_len <= r or heap[r] < heap[l]:
    #             nex = l
    #         else:
    #             nex = r
    #         if heap[p] < heap[nex]:
    #             heap[p], heap[nex] = heap[nex], heap[p]
    #             p = nex
    #         else:
    #             break
        
    # def build_heap(self, heap):
    #     for i in range(len(heap) - 1, -1, -1):
    #         self.max_heapify(heap, i, len(heap))

    # def heap_sort(self, nums):
    #     self.build_heap(nums)
    #     for i in range(len(nums) - 1, -1, -1):
    #         nums[i], nums[0] = nums[0], nums[i]
    #         self.max_heapify(nums, 0, i)
            
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     self.heap_sort(nums)
    #     return nums


# 2021.04.09 新的归并排序
class Solution2:
    def sortArray(self, nums):
        def merge(left, right):
            res = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res += left[i:]
            res += right[j:]
            return res
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        # 分
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        # 合并
        return merge(left, right)


# 2021.04.09 新的快速排序
class Solution3:
    def sortArray(self, nums):
        n = len(nums)

        def quick(left, right):
            if left >= right:
                return nums
            pivot = left
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[j] = nums[j], nums[pivot]
            quick(left, j - 1)
            quick(j + 1, right)
            return nums

        return quick(0, n - 1)
