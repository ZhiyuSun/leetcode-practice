"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
# 2021.04.07 我居然做出了哈希法
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target <= 2: return []
        dic = {}
        s = 0
        dic[0] = -1
        dic[1] = 0
        dic[3] = 1
        # [1,2,3,4,5]
        s = 3
        res = []
        for i in range(2, target):
            s += i+1
            dic[s] = i
            if s - target in dic:
                if i - dic[s - target]  >=2:
                    res.append([k+2 for k in range(dic[s - target], i)])
        return res


# 2021.04.07 大神解法，滑动窗口
class Solution1:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1 # 滑动窗口的左边界
        j = 1 # 滑动窗口的右边界
        sum = 0 # 滑动窗口中数字的和
        res = []

        while i <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += j
                j += 1
            elif sum > target:
                # 左边界向右移动
                sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                sum -= i
                i += 1

        return res


# 2021.04.07 路飞哥的解法，数学法
class Solution2:
    def findContinuousSequence(self, target: int):
        i, j, res = 1, 2, []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res



# 2021.04.07 我的优化版
class Solution3:
    def findContinuousSequence(self, target: int):
        if target <= 2: return []
        dic = {0:-1}
        s, res = 0, []
        for i in range(target//2 + 1):
            s += i+1
            dic[s] = i
            if s - target in dic:
                if i - dic[s - target]  >=2:
                    res.append(list(range(dic[s - target] + 2, i + 2)))
        return res