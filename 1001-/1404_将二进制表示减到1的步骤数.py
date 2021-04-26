"""
给你一个以二进制形式表示的数字 s 。请你返回按下述规则将其减少到 1 所需要的步骤数：

如果当前数字为偶数，则将其除以 2 。

如果当前数字为奇数，则将其加上 1 。

题目保证你总是可以按上述规则将测试用例变为 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.04.26 犯规解法
class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)
        count = 0
        while n != 1:
            if n % 2 == 1:
                n += 1
            else:
                n //= 2
            count += 1
            print(n)
        return count


# 2021.04.26 找规律的方法很强
class Solution1:
    def numSteps(self, s: str) -> int:
        n, ans = len(s), 0
        # meet1 记录我们有没有遇见过字符 1
        meet1 = False
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                # 如果当前字符为 0，分为两种情况
                # (1) 还没有遇见过字符 1，那么这个 0 是字符串低位的 0，需要一次除二操作
                # (2) 遇见过字符 1，那么这个 0 会因为它右侧的某次加一操作变为 1，因此它需要一次加一和一次除二操作
                ans += (2 if meet1 else 1)
            else:
                # 如果当前字符为 1，分为两种情况
                # (1) 还没有遇见过字符 1，那么这个 1 需要一次加一和一次除二操作
                #     这里需要考虑一种特殊情况，就是这个 1 是字符串最左侧的 1，它并不需要任何操作
                # (2) 遇见过字符 1，那么这个 1 会因为它右侧的某次加一操作变为 0，因此它只需要一次除二操作
                if not meet1:
                    if i != 0:
                        ans += 2
                    meet1 = True
                else:
                    ans += 1
        return ans
