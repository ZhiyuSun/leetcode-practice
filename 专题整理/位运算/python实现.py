from typing import List
from functools import reduce
# 191. 位1的个数
class Solution191:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
    
    def hammingWeight1(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count

# 231. 2的幂
class Solution231:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
    def isPowerOfTwo1(self, n: int) -> bool:
        if n == 0: return False
        return n & (n-1) == 0

# 338. 比特位计数
class Solution338:
    def countBits(self, num: int) -> List[int]:
        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones
        
        bits = [countOnes(i) for i in range(num + 1)]
        return bits

    def countBits1(self, num: int) -> List[int]:
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i&(i-1)] + 1)
        return bits

# 136. 只出现一次的数字
class Solution136:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] ^= nums[i-1]
        return nums[-1]
    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

# 168. Excel表列名称
class Solution171:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n:
            n -= 1
            s = chr(65 + n % 26) + s
            n //= 26
        return s
# 171. Excel表列序号
class Solution1171:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum([(ord(columnTitle[i]) - ord('A') + 1)*26**(len(columnTitle)-i-1) for i in range(len(columnTitle))])