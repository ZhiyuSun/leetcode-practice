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
