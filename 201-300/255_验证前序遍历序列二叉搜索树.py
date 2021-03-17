"""
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。

你可以假定该序列中的数都是不相同的。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [5,2,6,1,3]
输出: false
示例 2：

输入: [5,2,1,3,6]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.03.17 题目都看不懂
from typing import List
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        #局部递减  整体递增
        dec_stack = []
        pre_max = -0x3f3f3f3f       #左下点的位置（一条左上至右下的斜线分割，斜线上最左上的点）
        for x in preorder:
            if pre_max > x:         #右侧的，要比左边的大（整体递增）
                return False
            while dec_stack and dec_stack[-1] <= x: #（维持局部递减）
                pre_max = dec_stack.pop()
            
            dec_stack.append(x)
        
        return True
