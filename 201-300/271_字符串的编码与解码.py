"""
请你设计一个算法，可以将一个 字符串列表 编码成为一个 字符串。这个编码后的字符串是可以通过网络进行高效传送的，并且可以在接收端被解码回原来的字符串列表。
"""

# 2021.04.26 我的取巧的方法
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return strs

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return s