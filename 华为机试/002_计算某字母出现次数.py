"""
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写。

输入描述:
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字母。

输出描述:
输出输入字符串中含有该字符的个数。
"""

def ge_num():
    fir_line = input()
    sec_line = input()
    if len(sec_line) == 0 or len(sec_line) >1:
        return "第二行填入一个字符："
    leng = len(fir_line.strip().lower().split(sec_line.lower()))-1

    return leng

print(ge_num())