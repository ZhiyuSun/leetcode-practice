from typing import List
import random
# 912. 排序数组
class Solution912:
    # 冒泡排序
    def bubble_sort(self, nums: List[int]) -> List[int]:
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

    # 插入排序
    def insert_sort(self, nums: List[int]) -> List[int]:
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

    # 选择排序
    def select_sort(self, nums: List[int]) -> List[int]:
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
    
    # 归并排序
    def merge_sort(self, nums: List[int]) -> List[int]:
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
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        # 合并
        return merge(left, right)

    # 快速排序
    def quick_sort(self, nums):
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
    
    def quick_sort1(self, nums):
        n = len(nums)

        def quick(left, right):
            if left >= right:
                return
            pivot = random.randint(left, right)
            i, j = left, right
            nums[left], nums[pivot] = nums[pivot], nums[left]

            while i < j:
                while i < j and nums[j] > nums[left]:
                    j -= 1
                while i < j and nums[i] <= nums[left]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[j] = nums[j], nums[left]
            quick(left, j - 1)
            quick(j + 1, right)
            return

        quick(0, n - 1)
        return nums
    
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