"""
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/score-after-flipping-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2020.12.7 直奔题解，贪心算法好
from typing import List
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # 行变换
        for i in range(len(A)):
            if A[i][0]==0:
                A[i]=[1-tmp for tmp in A[i]]
        # 列变换
        for j in range(1,len(A[0])):
            #每列1的个数比0少才变换
            cnt1=sum(A[i][j] for i in range(len(A)))
            if cnt1<len(A)/2:
                for i in range(len(A)):
                    A[i][j]=0 if A[i][j] else 1
        # 计算得分
        res=0
        for i in range(len(A)):
            t=A[i][::-1]
            item=[val*2**inx for inx,val in zip(range(len(t)),t)]
            res=res+sum(item)
        return int(res)
