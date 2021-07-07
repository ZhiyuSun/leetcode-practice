"""
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。

 

示例 1：

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-subarray-minimums
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.07.07 我的暴力法
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            cur_min = arr[i]
            for j in range(i, len(arr)):
                cur_min = min(cur_min, arr[j])
                res += cur_min
        return

# 2021.07.07 这题要用单调栈，可惜我这块完全不懂
class Solution1:
    def sumSubarrayMins(self, A: List[int]) -> int:
        A.append(-1)
        stack,res=[-1],0
        for i in range(len(A)):
            while A[i]<A[stack[-1]]:
                idx=stack.pop()
                res+=A[idx]*(i-idx)*(idx-stack[-1])
            stack.append(i)
        return res%(10**9+7)
