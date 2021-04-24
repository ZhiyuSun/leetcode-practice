"""
给你一个字符串形式的电话号码 number 。number 由数字、空格 ' '、和破折号 '-' 组成。

请你按下述方式重新格式化电话号码。

首先，删除 所有的空格和破折号。
其次，将数组从左到右 每 3 个一组 分块，直到 剩下 4 个或更少数字。剩下的数字将按下述规定再分块：
2 个数字：单个含 2 个数字的块。
3 个数字：单个含 3 个数字的块。
4 个数字：两个分别含 2 个数字的块。
最后用破折号将这些块连接起来。注意，重新格式化过程中 不应该 生成仅含 1 个数字的块，并且 最多 生成两个含 2 个数字的块。

返回格式化后的电话号码。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reformat-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 2021.04.24 有思路就行的题
class Solution:
    def reformatNumber(self, number: str) -> str:
        digit_arr = []
        for i in number:
            if i.isdigit():
                digit_arr.append(i)
        n_arr = []
        tmp = []
        for i in digit_arr:
            tmp.append(i)
            if len(tmp) == 3:
                n_arr.append(tmp[:])
                tmp = []
        if len(tmp) == 2:
            n_arr.append(tmp[:])
        if len(tmp) == 1:
            n_arr[-1].append(tmp[0])
        res = []
        for arr in n_arr:
            if len(arr) == 4:
                res.append(''.join(arr[:2]))
                res.append(''.join(arr[2:]))
            else:
                res.append(''.join(arr))
        return '-'.join(res)

# 2021.04.24 基本都是硬写，这个巧妙点
class Solution1:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ","").replace("-","")
        rem = len(number)%3
        num = len(number)//3 - 1 if rem in (0,1) else  len(number)//3

        ret = []
        for i in range(num):
            ret.append(number[i*3:(i+1)*3])
        if rem == 1:
            ret.append(number[num*3:num*3+2])
            ret.append(number[num*3+2:num*3+4])
        else:
            ret.append(number[num*3:])
        return '-'.join(ret)
        