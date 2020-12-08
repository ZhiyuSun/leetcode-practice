"""
给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。

形式上，斐波那契式序列是一个非负整数列表 F，且满足：

0 <= F[i] <= 2^31 - 1，（也就是说，每个整数都符合 32 位有符号整数类型）；
F.length >= 3；
对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。

返回从 S 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = list()

        def backtrack(index: int):
            if index == len(S):
                return len(ans) >= 3
            
            curr = 0
            for i in range(index, len(S)):
                if i > index and S[index] == "0":
                    break
                curr = curr * 10 + ord(S[i]) - ord("0")
                if curr > 2**31 - 1:
                    break
                
                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                elif len(ans) > 2 and curr > ans[-2] + ans[-1]:
                    break
        
            return False
        
        backtrack(0)
        return ans


# 网友的做法
class Solution1:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        m = 2 ** 31 - 1
        res = []
        n = len(S)
        def backtrack(pos):
            # 基线条件
            if pos == n:
                return len(res) > 2
            # 递归条件
            s = 0
            for i in range(pos, n):
                s = s * 10 + int(S[i])
                # 剪枝条件 1：当前项不能大于最大值
                if s > m:
                    break
                # 剪枝条件 2：当前项大于前两项之和，没有继续计算的必要
                if len(res) > 2 and s > res[-1] + res[-2]:
                    break
                # 剪枝条件 3：当前项以 0 开始，且不是 0 本身
                if S[pos] == '0' and i > pos:
                    break
                if len(res) < 2 or res[-1] + res[-2] == s:
                    # 保存现场
                    res.append(s)
                    # 回溯
                    if backtrack(i + 1):
                        return True
                    # 恢复现场
                    res.pop()
            return False
        return res if backtrack(0) else []