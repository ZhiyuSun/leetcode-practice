"""
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.25 完全不会，重在参与
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        n=len(arr)
        #删除尾部元素
        left=0#定义left=0是保证可以留下最开始的arr[0]
        for i in range(1,n):
            if arr[i]>=arr[i-1]:
                left=i
            else:
                break
        if left==n-1:
            return 0
        #删除头部元素
        right=n-1#定义right=n-1是保证可以留下最末尾的arr[n-1]
        for i in range(n-2,-1,-1):
            if arr[i]<=arr[i+1]:
                right=i
            else:
                break
        ans=min(n-left+1,right)
        #删除中间元素
        i=left
        j=right
        for i in range(left,-1,-1):
            j=right
            if arr[i]<=arr[right]:
                ans=min(ans,right-i-1)
                break
            while j<n and arr[i]>arr[j]:
                j+=1
            ans=min(ans,j-i-1)
        
        return ans
