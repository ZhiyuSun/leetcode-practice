"""
给你一个整数数组 arr 。

现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.20 没空慢慢看了，直奔题解
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        # 第一个哈希表
        # 其中有初始边界值 (0, 1)，表示异或和为 0（左边界，一个数都不选择）出现了 1 次
        freq = {0: 1}
        # 第二个哈希表
        # 其中有初始边界值 (0, 0)，表示异或和为 0（左边界，一个数都不选择）对应的 i 值为 0
        idsum = {0: 0}
        xorsum, ans = 0, 0
        # 枚举 k
        for k in range(n):
            # 计算前缀异或和
            xorsum ^= arr[k]
            # 如果这个前缀异或和之前出现过，那么就找到了一些满足要求的三元组
            if xorsum in freq:
                # 对应了题解中的公式 t * k - sum(i_t)
                ans += freq[xorsum] * k - idsum[xorsum]
            # 更新前缀异或和的出现次数
            freq[xorsum] = freq.get(xorsum, 0) + 1
            # 更新前缀异或和出现位置的下标之和
            # 注意 i-1 和 i 的关系，所以这里要额外增加 1
            idsum[xorsum] = idsum.get(xorsum, 0) + (k + 1)
        return ans
