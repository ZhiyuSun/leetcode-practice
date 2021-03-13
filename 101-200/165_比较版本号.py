#!/usr/bin/python
# -*- coding: utf-8 -*-

# 我的版本
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        number1 = version1.split('.')
        number2 = version2.split('.')
        length = max(len(number1), len(number2))

        for i in range(0, length):
            try:
                value1 = int(number1[i])
            except:
                value1 = 0
            
            try:
                value2 = int(number2[i])
            except:
                value2 = 0

            if value1 < value2:
                return -1
            elif value2 < value1:
                return 1
            else:
                i += 1
        return 0

s = Solution()
print(s.compareVersion("0", "1"))

# 其他的解法

class Solution1:
    def compareVersion(self, version1, version2):
        for x, y in itertools.zip_longest(version1.split("."), version2.split("."), fillvalue=0):
            if int(x) != int(y): return 1 if int(x) > int(y) else -1
        return 0

class Solution2:
    def compareVersion(self, version1, version2):
        vs1 = version1.split('.')
        vs2 = version2.split('.')
        n = min(len(vs1), len(vs2))
        for i in range(0, n):
            if int(vs1[i]) > int(vs2[i]):
                return 1
            elif int(vs1[i]) < int(vs2[i]):
                return -1
        if (vs1 > vs2):
            for x in vs1[n:]:
                if int(x) > 0:
                    return 1
            return 0
        if (vs2 > vs1):
            for x in vs2[n:]:
                if int(x) > 0:
                    return -1
            return 0
        return 0

class Solution3:
    def compareVersion(self, version1, version2):
        l_1 =version1.split('.')
        l_2 = version2.split('.')
        c =0
        while True:
            if c == len(l_1) and c==len(l_2):
                return 0
            if len(l_1)==c:
                l_1.append(0)
            if len(l_2)==c:
                l_2.append(0)
            if int(l_1[c])>int(l_2[c]):
                return 1
            elif int(l_1[c])<int(l_2[c]):
                return -1
            c+=1
