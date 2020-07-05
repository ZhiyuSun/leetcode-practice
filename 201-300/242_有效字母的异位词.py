class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        data = {}
        for i in s:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        for i in t:
            if not i in data:
                return False
            data[i] -= 1
        for i in data.values():
            if i != 0:
                return False
        return True

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return abs(sum([ord(x)**0.5 for x in s])-sum([ord(y)**0.5 for y in t]))<1e-5


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        se = set(s)
        if se == set(t):
            for i in se:
                # 直接比较字符元素个数比较字符的个数
                if s.count(i) != t.count(i):return False
            return True
        else:
            return False

class Solution5:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        se = set(s)
        for i in se:
            if s.count(i) != t.count(i):return False
        return True
