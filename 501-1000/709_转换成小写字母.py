"""
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
"""

# 2021.03.30 使用了函数库
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


class Solution1:
    def toLowerCase(self, str: str) -> str:
        s = []
        for i in str:
            if  65 <= ord(i) <= 90:
                s.append(chr(ord(i) + 32))
            else:
                s.append(i)
        return ''.join(s)


class Solution2:
    def toLowerCase(self, str: str) -> str:
        dic = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
               'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
               'M':'m', 'N':'n', 'O':'o','P':'p', 'Q':'q', 'R':'r',
               'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
               'Y':'y', 'Z':'z'}
        s = []
        for i in str:
            if dic.get(i):
                s.append(dic[i])
            else:
                s.append(i)
        return ''.join(s)

