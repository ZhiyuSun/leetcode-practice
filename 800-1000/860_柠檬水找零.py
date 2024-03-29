"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：

输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。
"""

from typing import List

# 我的解法
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        data = {5: 0, 10: 0}
        for i in bills:
            if i == 5:
                data[5] += 1
            if i == 10:
                if data[5] > 0:
                    data[5] -= 1
                    data[10] += 1
                else:
                    return False
            if i == 20:
                rest = 15
                if data[10] > 0:
                    data[10] -= 1
                    rest = 5
                if rest == 15:
                    if data[5] > 2:
                        data[5] -= 3
                    else:
                        return False
                else:
                    if data[5] > 0:
                        data[5] -= 1
                    else:
                        return False
        return True

# 官方解法。思路一样，但是精简很多
class Solution1: #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


# 2020.12.16 恢复信心
class Solution2:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coin_dict = {5: 0, 10: 0}
        for item in bills:
            if item == 5:
                coin_dict[5] += 1
            if item == 10:
                coin_dict[10] += 1
                if coin_dict[5] > 0:
                    coin_dict[5] -= 1
                else:
                    return False
            if item == 20:
                if coin_dict[5] == 0:
                    return False
                if coin_dict[10] > 0:
                    coin_dict[10] -= 1
                    coin_dict[5] -= 1
                else:
                    if coin_dict[5] > 2:
                        coin_dict[5] -= 3
                    else:
                        return False

        return True

# 2021.03.23 这题我写复杂了，但没想到曾经的自己也是这么写的，太没长进了
class Solution3:
    def lemonadeChange(self, bills: List[int]) -> bool:
        res = [0, 0]
        for i in bills:
            if i == 5:
                res[0] += 1
            if i == 10:
                if res[0] >= 1:
                    res[0] -= 1
                    res[1] += 1
                else:
                    return False
            if i == 20:
                cur = 20
                if res[1] >= 1:
                    res[1] -= 1
                    if res[0] >= 1:
                        res[0] -= 1
                    else:
                        return False
                else:
                    if res[0] >= 3:
                        res[0] -= 3
                    else:
                        return False
        return True

# 2021.03.23 重温官方解法
class Solution4:
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
