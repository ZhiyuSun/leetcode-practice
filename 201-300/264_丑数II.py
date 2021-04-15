class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for _ in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2: 
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
            


class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]


# 2021.04.15 我的解法，因为有重复项的存在，所以在查找值的时候，不要去break
class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        arr = [0] * n
        arr[0] = 1
        a, b, c = 0, 0, 0
        va, vb, vc = 2, 3, 5
        for i in range(1, n):
            arr[i] = min(va, vb, vc)
            count = 0
            for t in [va, vb, vc]:
                if arr[i] == t:
                    if count == 0:
                        a += 1
                        va = arr[a] * 2
                    elif count == 1:
                        b += 1
                        vb = arr[b] * 3
                    else:
                        c += 1
                        vc = arr[c] * 5
                count += 1
        return arr[-1]


# 2021.04.15 改进优化版
class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        arr = [0] * n
        arr[0] = 1
        a, b, c = 0, 0, 0
        va, vb, vc = 2, 3, 5
        for i in range(1, n):
            arr[i] = min(va, vb, vc)
            if arr[i] == va:
                a += 1
                va = arr[a] * 2
            if arr[i] == vb:
                b += 1
                vb = arr[b] * 3
            if arr[i] == vc:
                c += 1
                vc = arr[c] * 5
        return arr[-1]

# 2021.04.15 继续优化
class Solution3:
    def nthUglyNumber(self, n: int) -> int:
        arr = [0] * n
        arr[0] = 1
        a = b = c = 0
        for i in range(1, n):
            arr[i] = min(arr[a] * 2, arr[b] * 3, arr[c] * 5)
            if arr[i] == arr[a] * 2:
                a += 1
            if arr[i] == arr[b] * 3:
                b += 1
            if arr[i] == arr[c] * 5:
                c += 1
        return arr[-1]

import heapq
# 2021.04.15 官方解法1， 最小堆
class Solution4:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for _ in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                nxt = curr * factor
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)

# 2021.04.15 官方解法，动态规划
class Solution5:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1

        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        
        return dp[n]

