"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""


from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        size = len(nums)
        if size < 4: return res
        nums.sort()
        for a in range(0, size-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, size-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c, d = b+1, size-1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c+1] == nums[c]:
                            c += 1
                        while c < d and nums[d-1] == nums[d]:
                            d -= 1
                        c += 1
                        d -= 1
        return res


# 高速解法
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort()
        result = []

        for idx in range(len(nums) - 3):
            if nums[idx] + nums[idx+1] * 3 > target: break  # 这是加速项目，如果当前位置的数字+剩余位置数位的下一个数的倍数>target，则分析当前位置无意义
            if idx > 0 and nums[idx] == nums[idx - 1]: continue  # 如果当前的索引已经不是第一位的了，就要走到一个跟上一个不一样数字的索引上去
            if nums[idx] + nums[-1] * 3 < target: continue  # 这是加速项目，如果当前位置的数字+剩余位置数位的最后（大）数的倍数<target，则分析当前位置无意义

            for i in range(idx+1, len(nums)-2):
                if nums[idx] + nums[i] + nums[i + 1] * 2 > target: break
                if nums[idx] + nums[i] + nums[-1] * 2 < target: continue
                if i > idx+1 and nums[i] == nums[i-1]: continue

                j, k = i + 1, len(nums) - 1
                while j < k:
                    s = nums[idx] + nums[i] + nums[j] + nums[k]
                    if s > target:
                        k -= 1
                    elif s < target:
                        j += 1
                    else:
                        result.append([nums[idx], nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]: j += 1
                        while j < k and nums[k] == nums[k - 1]: k -= 1
                        j += 1
                        k -= 1
        return result

# 我新写的
class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        size = len(nums)
        if size < 4: return res
        nums.sort()
        for a in range(0, size-3):
            if nums[a] + nums[a+1] * 3 > target: break
            if nums[a] + nums[-1] * 3 < target: continue
            if a > 0 and nums[a] == nums[a-1]: continue
            for b in range(a+1, size-2):
                if nums[a] + nums[b] + nums[b+1] * 2 > target: break
                if nums[a] + nums[b] + nums[-1] * 2 < target: continue
                if b > a+1 and nums[b] == nums[b-1]: continue
                c, d = b+1, size-1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] < target: c += 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target: d -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c+1] == nums[c]: c += 1
                        while c < d and nums[d-1] == nums[d]: d -= 1
                        c += 1
                        d -= 1
        return res