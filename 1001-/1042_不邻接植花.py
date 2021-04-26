"""

有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi 的双向路径。在每个花园中，你打算种下四种花之一。

另外，所有花园 最多 有 3 条路径可以进入或离开.

你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。

以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1、2、3、4 表示。保证存在答案。

"""
from typing import List

from collections import defaultdict

# 2021.04.26 原来可以很简单
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        for u, v in paths:
            G[u].append(v)
            G[v].append(u)
        ans = [0] * n
        for u in range(1, n + 1):
            colors = set(range(1, 5)) - set(ans[v - 1] for v in G[u])
            ans[u - 1] = colors.pop()
        return ans
