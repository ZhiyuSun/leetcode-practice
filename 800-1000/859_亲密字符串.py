"""
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。

 

示例 1：

输入： A = "ab", B = "ba"
输出： true
解释： 你可以交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 相等。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/buddy-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 2021.07.03 直奔题解
# 思路很重要
# 返回true情况：
# 大条件：len(A) == len(B)
# 一：有两个不同地方(i,j)，且A[i]=B[j],A[j]=B[i]
# 二：完全相同，一个数组中存在重复数字

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        index =[]
        if len(A) == len(B):
            for i in range(len(A)):
                if A[i] != B[i]:
                    index.append(i)
            if len(index) == 2 and A[index[0]] == B[index[1]] and A[index[1]] == B[index[0]]:
                return True
            if len(index) == 0 and len(A)-len(set(A)) > 0:
                return True
        return False


# 2021.07.03 另一种做法
class Solution2:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): # 长度不相等必定不符合
            return False

        idx =[i for i in range(len(A))  if A[i] != B[i]]  
        if len(idx) == 2 and A[idx[0]] == B[idx[1]] and A[idx[1]] == B[idx[0]]:  # 两个字符串交换两次完全相同
            return True
        if len(idx) == 0 and len(A)-len(set(A)) > 0:  # 字符串完全相同，且单个字母出现超过两次(超过两次的字母交换不影响)
            return True

        return False
