"""
有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，请你按下述规则为栅栏设计涂色方案：

每个栅栏柱可以用其中 一种 颜色进行上色。
相邻的栅栏柱 最多连续两个 颜色相同。
给你两个整数 k 和 n ，返回所有有效的涂色 方案数 。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paint-fence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.04.15 直奔题解，很巧妙，动态规划
class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                dp[1] = k
            elif i == 2:
                dp[2] = k * k
            else:
                dp[i] = dp[i-2] * (k-1) + dp[i-1] * (k-1)
        return dp[n]


# 2021.04.15 清晰易懂的解法，比较容易想到
# dp[i][0] = (k - 1) * (dp[i - 1][0] + dp[i - 1][1])  # 即i-1已经占用了一种颜色，i和i-1颜色不同，那么i可以用剩下的k-1种方案，随便和i-1搭配
# dp[i][1] = dp[i - 1][0]  # i和i-1颜色一样，那么方案数就是 i-1 和 i-2颜色不同的那些方案，不然的话就违反了题目要求，最多两个同颜色相连

class Solution1:
    def numWays(self, n: int, k: int) -> int:
        if not n or not k: return 0

        dp = [[0, 0] for _ in range(n)]
        dp[0] = [k, 0]

        for i in range(1, n):
            dp[i][0] = (k - 1) * sum(dp[i - 1])
            dp[i][1] = dp[i - 1][0]

        return sum(dp[n - 1])
