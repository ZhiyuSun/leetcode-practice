"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.11.09 融会贯通的小孙
from typing import List

# 排序
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]

# 时间复杂度：O(nlogn)，其中 n 是数组 arr 的长度。算法的时间复杂度即排序的时间复杂度。
# 空间复杂度：O(logn)，排序所需额外的空间复杂度为 O(logn)。


# 堆
import heapq
class Solution1:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

# 时间复杂度：O(nlogk)，其中 n 是数组 arr 的长度。由于大根堆实时维护前 k 小值，所以插入删除都是 O(logk) 的时间复杂度，
# 最坏情况下数组里 n 个数都会插入，所以一共需要 O(nlogk) 的时间复杂度。
# 空间复杂度：O(k)，因为大根堆里最多 k 个数。


# 扩展：找第K大的数，topK问题
# 解法：全局排序

# 2021.02.07 再战经典题
# 首先是排序思路，这种方法是O(nlogn)
class Solution2:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[0:k]

# 然后我想到的是选择排序，只要前k个，那么实际复杂度就是O(kn),某个用例会超时
class Solution3:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        for i in range(k):
            lowest_index = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[lowest_index]:
                    lowest_index = j
            arr[i], arr[lowest_index] = arr[lowest_index], arr[i]
        return arr[0:k]

# 利用heapq建堆，但是还是记不住
class Solution4:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans
# Python的堆是小根堆，每入栈一个元素，会把最小的去除。所以要把每个数据反一下

# 快排思想
import random
class Solution5:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):
        pos = self.randomized_partition(arr, l, r)
        num = pos - l + 1
        if k < num:
            self.randomized_selected(arr, l, pos - 1, k)
        elif k > num:
            self.randomized_selected(arr, pos + 1, r, k - num)

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]

# 2021.03.21 又忘记了api
class Solution6:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(0, len(arr)-k):
            heapq.heappush(heap, arr[i])
        res = []
        for i in range(len(arr)-k, len(arr)):
            heapq.heappush(heap, arr[i])
            res.append(heapq.heappop(heap))
        return res

# 2021.03.21 磕磕绊绊
class Solution7:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        res =[-i for i in arr[:k]]
        heapq.heapify(res)
        for i in arr[k:]:
            if -i > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, -i)
        return [-i for i in res]