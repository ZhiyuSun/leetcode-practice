"""
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。

设计一个算法使得这 m 个子数组各自和的最大值最小。

"""

# 2021.03.30 直奔题解，这题的思路很巧妙
from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #二分查找

        #指定二分查找范围
        left, right = max(nums), sum(nums)

        #定义 测试中点是大还是小的 测试函数
        def test_mid(mid):
            #初始化
            num = 1 #num表示使用该mid我们会得到几个数组
            s = 0 #s表示当前数组的和

            for i in nums:
                if s+i > mid: #如果当前数组已经超过mid，要停止这个数组
                    s = i #这个数变为下一个数组的开头
                    num += 1 #会得到的数组数量+1
                else:
                    s += i

            return num > m #数组总数是否>m, 大于的话说明mid太小，二分查找取右边
            #这里有一个注意点，如果num已经等于m了, 但此时如果left不等于right，范围还是会继续收敛的，
            #且取的是左半边，目的是让我们能最终找到一个确切的值，这个值恰好就是取得了最大值的那个数组的和
            #(因为小于这个和的话，就不能通过num=m的测试；而大于这个m的话，即使通过了num=m的测试，
            #范围也会继续向左边收敛，直到我们找到的就是这个和)。
        
        #进行二分查找
        while left < right: #当left == right的时候就终止查找，返回任意一个
            mid = (left + right) // 2
            if_right = test_mid(mid)
            if if_right:
                left = mid+1
            else:
                right = mid #num <= m的情况

        return left
