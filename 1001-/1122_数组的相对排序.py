"""
给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

 

示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/relative-sort-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import collections

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        return sorted(arr1, key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))


class Solution1:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
       #将arr1 counter计数，按照arr2来取
        li = []
        counter = collections.Counter
        count = counter(arr1)
        #按照arr2将arr1的元素存入li
        for val in arr2:
            if val in count:
                l = count[val]
                print(l)
                for i in range(l):
                    li.append(val)
            #被存的元素删除掉
            del count[val]
        #剩下的元素排序放到末尾
        li += sorted(list(count.elements()))
        return li

# 2021.03.30 活用计数排序
class Solution2:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = [0 for _ in range(1001)]  # 由于题目说 arr1 的范围在 0-1000，所以生成一个 1001 大小的数组用来存放每个数出现的次数。
        ans = []  # 储存答案的数组。
        for i in range(len(arr1)):  # 遍历 arr1，把整个arr1的数的出现次数储存在 arr 上，arr 的下标对应 arr1 的值，arr 的值对应 arr1 中值出现的次数。
            arr[arr1[i]] += 1  # 如果遇到了这个数，就把和它值一样的下标位置上 +1，表示这个数在这个下标 i 上出现了 1 次。
        for i in range(len(arr2)):  # 遍历 arr2，现在开始要输出答案了。
            while arr[arr2[i]] > 0:  # 如果 arr2 的值在 arr 所对应的下标位置出现次数大于 0，那么就说明 arr 中的这个位置存在值。
                ans.append(arr2[i])  # 如果存在值，那就把它加到 ans 中，因为要按 arr2 的顺序排序。
                arr[arr2[i]] -= 1  # 加进去了次数 -1 ，不然就死循环了。
        for i in range(len(arr)):  # 如果 arr1 的值不在 arr2 中，那么不能就这么结束了，因为题目说了如果不在，剩下的值按照升序排序。
            while arr[i] > 0:  # 同样也是找到大于 0 的下标，然后一直加到 ans 中，直到次数为 0。
                ans.append(i)
                arr[i] -= 1
        return ans  # 返回最终答案。
