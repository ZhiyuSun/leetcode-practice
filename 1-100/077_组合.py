from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 先把不符合条件的情况去掉
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        # 当前已经找到的组合存储在 pre 中，需要从 start 开始搜索新的元素
        # 在第 k 层结算
        if len(pre) == k:
            res.append(pre[:])
            return

        for i in range(start, n + 1):
            pre.append(i)
            # 因为已经把 i 加入到 pre 中，下一轮就从 i + 1 开始
            # 注意和全排列问题的区别，因为按顺序选择，因此无须使用 used 数组
            self.__dfs(i + 1, k, n, pre, res)
            # 回溯的时候，状态重置
            pre.pop()


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 特判
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, pre, res):
        if len(pre) == k:
            res.append(pre[:])
            return

        # 注意：这里 i 的上限是归纳得到的
        for i in range(start, n - (k - len(pre)) + 2):
            pre.append(i)
            self.__dfs(i + 1, k, n, pre, res)
            pre.pop()


# 2021.02.03 模仿回溯的思路，终于写出来了
class Solution3:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrace(cur, index):
            if len(cur) == k:
                res.append(cur)
            for i in range(index, n):
                if used[i] == 1:
                    continue
                used[i] = 1
                backtrace(cur + [i+1], i+1)
                used[i] = 0

        used = [0] * n
        res = []
        backtrace([], 0)
        return res

# 经验总结：
# 有个数组，专门去做标记
# 依然可以使用内部函数
# 一开始发现有重，后来增加一个新的索引参数可解决问题


# 2021.02.03 优化版，因为是按顺序选择，所以无需used数组
class Solution4:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrace(cur, index):
            if len(cur) == k:
                res.append(cur)
            for i in range(index, n):
                backtrace(cur + [i+1], i+1)

        res = []
        backtrace([], 0)
        return res