"""
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.13 我的解法，掌控回溯
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        def _dfs(level, path, rest):
            if level == 4:
                if not rest:
                    res.append('.'.join(path))
                return
            if not rest:
                return

            path.append(rest[0])
            _dfs(level+1, path, rest[1:])
            path.pop()

            if rest[0] != '0':
                if len(rest) > 1:
                    path.append(rest[0:2])
                    _dfs(level + 1, path, rest[2:])
                    path.pop()
                if len(rest) > 2 and int(rest[0:3]) <= 255:
                    path.append(rest[0:3])
                    _dfs(level + 1, path, rest[3:])
                    path.pop()

        res = []
        _dfs(0, [], s)
        return res

# 2021.04.13 简单点，思考问题的方式简单点
class Solution2:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        def _dfs(level, path, rest):
            if level == 4:
                if not rest:
                    res.append('.'.join(path))
                return
            if len(rest) < (4-level) or len(rest) > (4-level) * 3:
                return
            _dfs(level+1, path+[rest[0]], rest[1:])
            if rest[0] != '0':
                if len(rest) > 1:
                    _dfs(level + 1, path+[rest[0:2]], rest[2:])
                if len(rest) > 2 and int(rest[0:3]) <= 255:
                    _dfs(level + 1, path+[rest[0:3]], rest[3:])

        res = []
        _dfs(0, [], s)
        return res