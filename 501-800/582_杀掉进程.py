"""
系统中存在 n 个进程，形成一个有根树结构。给你两个整数数组 pid 和 ppid ，其中 pid[i] 是第 i 个进程的 ID ，ppid[i] 是第 i 个进程的父进程 ID 。

每一个进程只有 一个父进程 ，但是可能会有 一个或者多个子进程 。只有一个进程的 ppid[i] = 0 ，意味着这个进程 没有父进程 。

当一个进程 被杀掉 的时候，它所有的子进程和后代进程都要被杀掉。

给你一个整数 kill 表示要杀掉​​进程的 ID ，返回杀掉该进程后的所有进程 ID 的列表。可以按 任意顺序 返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kill-process
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import defaultdict, deque

# 2021.04.25 直奔题解
# 我的经验是，遇到图的题目，不用慌，找到它的表示方法，例如字典，然后用BFS就行了
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(set)

        for p, pp in zip(pid, ppid):
            graph[pp].add(p)

        ans = []
        d = deque()
        d.append(kill)
        while d:
            cur = d.popleft()
            ans.append(cur)
            d.extend(graph[cur])

        return ans
