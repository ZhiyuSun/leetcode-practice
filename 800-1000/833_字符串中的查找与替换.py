"""
某个字符串 S 需要执行一些替换操作，用新的字母组替换原有的字母组（不一定大小相同）。

每个替换操作具有 3 个参数：起始索引 i，源字 x 和目标字 y。规则是：如果 x 从原始字符串 S 中的位置 i 开始，那么就用 y 替换出现的 x。如果没有，则什么都不做。

举个例子，如果 S = “abcd” 并且替换操作 i = 2，x = “cd”，y = “ffff”，那么因为 “cd” 从原始字符串 S 中的位置 2 开始，所以用 “ffff” 替换它。

再来看 S = “abcd” 上的另一个例子，如果一个替换操作 i = 0，x = “ab”，y = “eee”，以及另一个替换操作 i = 2，x = “ec”，y = “ffff”，那么第二个操作将不会执行，因为原始字符串中 S[2] = 'c'，与 x[0] = 'e' 不匹配。

所有这些操作同时发生。保证在替换时不会有任何重叠： S = "abc", indexes = [0, 1], sources = ["ab","bc"] 不是有效的测试用例。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-and-replace-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
# 2021.04.09 直奔题解，是我看不懂的解法
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse = True):
            if all(i+k < len(S) and S[i+k] == x[k] for k in range(len(x))):
                S[i:i+len(x)] = list(y)

        return "".join(S)
