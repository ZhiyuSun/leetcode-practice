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
class Solution1(object): #aw
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
