"""
猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
返回我选出的数字。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 20021.04.07 二分法，秒过

def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 1, n
        while i <= j:
            mid = i + (j-i)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                i = mid + 1
            else:
                j = mid - 1
        return 0

# 2021.04.07 计算二分可以用移位
class Solution1:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) >> 1
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid - 1
            elif guess(mid) == 1:
                l = mid + 1
